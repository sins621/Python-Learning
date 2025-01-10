from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[String] = mapped_column(String(250), unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[String] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[String] = mapped_column(String(250), nullable=False)
    img_url: Mapped[String] = mapped_column(String(250), nullable=False)

    def __init__(self, **kw):
        self.title = kw.get("title", None)
        self.year = kw.get("year", None)
        self.description = kw.get("description", None)
        self.rating = kw.get("rating", None)
        self.ranking = kw.get("ranking", None)
        self.review = kw.get("review", None)
        self.img_url = kw.get("img_url", None)


class EditForm(FlaskForm):
    new_rating = StringField("Your Rating Out of 10", validators=[DataRequired()])
    new_review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    movies_query = db.session.execute(
        db.select(Movie).order_by(Movie.ranking.desc())
    ).scalars()
    return render_template("index.html", movies=movies_query)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    movie_id = request.args.get("movie_id")
    edit_form = EditForm()
    movie_query = db.session.execute(
        db.select(Movie).where(Movie.id == movie_id)
    ).scalar()
    if edit_form.validate_on_submit():
        if movie_query != None:
            print(edit_form.new_rating.data)
            print(edit_form.new_review.data)
            movie_query.rating = edit_form.new_rating.data
            movie_query.review = edit_form.new_review.data
            db.session.commit()
            return redirect("/")
        else:
            print("movie_query is none")
            return redirect("/")
    return render_template("edit.html", form=edit_form, movie=movie_query)


@app.route("/delete", methods=["POST", "GET"])
def delete():
    movie_id = request.args.get("movie_id")
    movie_query = db.session.execute(
        db.select(Movie).where(Movie.id == movie_id)
    ).scalar()
    if movie_query != None:
        db.session.delete(movie_query)
        db.session.commit()
    else:
        return "Unlucky"
    return redirect("/")


# Create
# with app.app_context():
#     db.create_all()
#     new_book = Book(title="pussy Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()


@app.route("/add")
def add():
    return ""


if __name__ == "__main__":
    app.run(debug=True)
