from datetime import date
from functools import wraps

from flask import Flask, abort, flash, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_user,
    logout_user,
    login_required,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash, generate_password_hash

# Import your forms from the forms.py
from forms import CreateLoginForm, CreatePostForm, CreateRegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "seeeeecretwow"
login_manager = LoginManager()
login_manager.init_app(app)
ckeditor = CKEditor(app)
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __init__(self, title, subtitle, date, body, author, img_url):
        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.body = body
        self.author = author
        self.img_url = img_url


# TODO: Create a User table for all your registered users.
class Users(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)


with app.app_context():
    db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
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
        new_user = Users(
            email=register_form.email.data,
            name=register_form.name.data,
            password=secure_password,
        )
        try:
            result = db.session.execute(db.select(Users))
            users = result.scalars().all()
            if users:
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect("/")
        except SQLAlchemyError as e:
            return f"Database Error: {e}"
    return render_template("register.html", form=register_form)


# TODO: Retrieve a user from the database based on their email.
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = CreateLoginForm()
    if login_form.validate_on_submit():
        assert login_form.email.data is not None
        assert login_form.password.data is not None

        email = login_form.email.data
        password = login_form.password.data
        try:
            result = db.session.execute(db.select(Users).where(Users.email == email))
            user = result.scalar()
            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect("/about")
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
@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
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
        author=post.author,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        assert edit_form.title.data is not None
        assert edit_form.subtitle.data is not None
        assert edit_form.img_url.data is not None
        assert edit_form.body.data is not None
        assert current_user is not None

        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = str(current_user)
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
