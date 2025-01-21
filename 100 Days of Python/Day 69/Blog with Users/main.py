from datetime import date
from functools import wraps

from flask import Flask, abort, flash, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash, generate_password_hash

# Import your forms from the forms.py
from forms import CreateLoginForm, CreatePostForm, CreateRegisterForm, CreateCommentForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "seeeeecretwow"
login_manager = LoginManager()
login_manager.init_app(app)
ckeditor = CKEditor(app)
Bootstrap5(app)


# CREATE DATABASE


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    posts = db.relationship("BlogPost", backref="user", cascade="all, delete")
    comments = db.relationship("Comment", backref="user", cascade="all, delete")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = db.relationship("Comment", backref="blogpost", cascade="all, delete")

    def __init__(self, title, subtitle, date, body, author_id, img_url):
        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.body = body
        self.author_id = author_id
        self.img_url = img_url


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"), nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def __init__(self, author_id, post_id, comment):
        self.author_id = author_id
        self.post_id = post_id
        self.comment = comment


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            if current_user.id != 1:
                return abort(403)
        else:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)


with app.app_context():
    db.create_all()


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = CreateRegisterForm()
    if register_form.validate_on_submit():
        assert register_form.email.data is not None
        assert register_form.name.data is not None
        assert register_form.password.data is not None
        secure_password = generate_password_hash(
            register_form.password.data, method="pbkdf2", salt_length=16
        )
        new_user = User(
            email=register_form.email.data,
            name=register_form.name.data,
            password=secure_password,
        )
        try:
            user = User.query.filter_by(email=new_user.email).scalar()
            print(user)
            if user:
                flash("Email Already in Use")
                redirect("url_for('register')")
            else:
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect("/")
        except SQLAlchemyError as e:
            return f"Database Error: {e}"
    return render_template("register.html", form=register_form)


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = CreateLoginForm()
    if login_form.validate_on_submit():
        assert login_form.email.data is not None
        assert login_form.password.data is not None

        email = login_form.email.data
        password = login_form.password.data
        try:
            user = User.query.filter_by(email=email).scalar()

            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect("/")
                else:
                    flash("Incorrect Username or Password")
                    return redirect(url_for("login"))
            else:
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))
        except SQLAlchemyError as e:
            return f"Database Error: {e}"
    return render_template("login.html", form=login_form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("get_all_posts"))


@app.route("/")
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CreateCommentForm()
    comments = Comment.query.filter_by(post_id=post_id)

    if comment_form.validate_on_submit():
        assert comment_form.comment.data is not None
        assert current_user.id is not None
        new_comment = Comment(
            comment=comment_form.comment.data,
            author_id=current_user.id,
            post_id=post_id,
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    return render_template(
        "post.html", form=comment_form, post=requested_post, comments=comments
    )


@app.route("/new-post", methods=["GET", "POST"])
@admin_required
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        assert form.title.data is not None
        assert form.subtitle.data is not None
        assert form.img_url.data is not None
        assert form.body.data is not None
        assert current_user.id is not None

        print(current_user.id)
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author_id=current_user.id,
            date=date.today().strftime("%B %d, %Y"),
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author_id=post.author_id,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        assert edit_form.title.data is not None
        assert edit_form.subtitle.data is not None
        assert edit_form.img_url.data is not None
        assert edit_form.body.data is not None
        assert current_user.id is not None

        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author_id = current_user.id
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
@admin_required
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    # comments_to_delete = Comment.query.filter_by(post_id=post_id)
    db.session.delete(post_to_delete)
    # db.session.delete(comments_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
@admin_required
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
