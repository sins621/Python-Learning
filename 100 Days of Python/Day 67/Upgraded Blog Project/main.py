from datetime import date

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor, CKEditorField
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired, Length

app = Flask(__name__)
app.config["SECRET_KEY"] = "SUPERSECRETOMG"
Bootstrap5(app)
ckeditor = CKEditor(app)
today = date.today()


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class BlogPost(db.Model):
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


class PostForm(FlaskForm):
    title = StringField("Post Title", validators=[DataRequired(), Length(max=250)])
    subtitle = StringField("Subtitle", validators=[DataRequired(), Length(max=250)])
    author_name = StringField(
        "Author Name", validators=[DataRequired(), Length(max=250)]
    )
    img_url = StringField(
        "Image URL", validators=[DataRequired(), URL(), Length(max=250)]
    )
    body = CKEditorField("Post Body", validators=[DataRequired()])
    submit = SubmitField("Submit", id="submit")


def db_has_title(db_object, db_list):
    for db_item in db_list:
        if db_object.title == db_item.title:
            return True
    return False


with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts():
    # DONE: Query the database for all the posts. Convert the data to a python list.
    posts = (
        db.session.execute(db.select(BlogPost).order_by(BlogPost.id)).scalars().all()
    )
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route("/<int:post_id>")
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(
        BlogPost, post_id, description="Sorry, Blog Post not Available"
    )
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    new_post_form = PostForm()
    if new_post_form.validate_on_submit():
        try:
            new_post_query = BlogPost(
                title=new_post_form.title.data,
                subtitle=new_post_form.subtitle.data,
                date=today.strftime("%B %d, %Y"),
                body=new_post_form.body.data,
                author=new_post_form.author_name.data,
                img_url=new_post_form.img_url.data,
            )
            result = db.session.execute(db.select(BlogPost).order_by(BlogPost.title))
            all_posts = result.scalars().all()
            if db_has_title(new_post_query, all_posts):
                return f"{new_post_query.title} Was Already Submitted", 400
            else:
                db.session.add(new_post_query)
                db.session.commit()
                return redirect("/")
        except SQLAlchemyError as e:
            return f"Database error {e} occured", 500
    return render_template("make-post.html", form=new_post_form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = PostForm(
        title=post.title,
        subtitle=post.subtitle,
        body=post.body,
        author_name=post.author,
        img_url=post.img_url,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.body = edit_form.body.data
        post.author = edit_form.author_name.data
        post.img_url = edit_form.img_url.data
        try:
            db.session.commit()
            return redirect(url_for("show_post", post_id=post.id))
        except SQLAlchemyError as e:
            return f"Database error {e} occured", 500
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete-post/<int:post_id>")
def delete_post(post_id):
    post_to_delete = BlogPost.query.get_or_404(
        post_id, description=f"Cafe at ID:{post_id} not Found"
    )
    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect("/")
    except SQLAlchemyError as e:
        return f"Database error {e} occured", 500


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
