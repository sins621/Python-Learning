import os
import json

import requests
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

load_dotenv()
movie_db_key = os.getenv("MOVIE_DB_KEY")


app = Flask(__name__)

# Unimportant Key
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)

movie_search_url = "https://api.themoviedb.org/3/search/movie"
movie_search_headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZDQ1NzVjZTQ4YTkyY2VlYThlYjIwODQwNGJiMzJhZCIsIm5iZiI6MTczNjU0MTg1Ny4zNDQsInN1YiI6IjY3ODE4NmExMjE4ZmQ1N2FjZjRlYmEwYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5PzMFTRcbYBJ-HArLtyhL7JnwbSeO4dgY6CVGLTIOA8",
}


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[String] = mapped_column(String(), unique=True)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[String] = mapped_column(String())
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[int] = mapped_column(Integer)
    review: Mapped[String] = mapped_column(String())
    img_url: Mapped[String] = mapped_column(String())

    def __init__(self, **kw):
        self.title = kw.get("title", None)
        self.year = kw.get("year", None)
        self.description = kw.get("description", None)
        self.rating = kw.get("rating", None)
        self.ranking = kw.get("ranking", None)
        self.review = kw.get("review", None)
        self.img_url = kw.get("img_url", None)


class EditForm(FlaskForm):
    new_ranking = StringField("Your Ranking Out of 10", validators=[DataRequired()])
    new_review = StringField("Your Review", validators=[DataRequired()])
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
            print(edit_form.new_ranking.data)
            print(edit_form.new_review.data)
            movie_query.ranking = edit_form.new_ranking.data
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
    return redirect(url_for("home"))


class AddForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/add_form", methods=["POST", "GET"])
def add_form():
    add_form = AddForm()
    if add_form.validate_on_submit():
        return redirect(url_for("select", movie_title=add_form.movie_title.data))
    return render_template("add.html", form=add_form)


@app.route("/add_movie")
def add_movie():
    movie_title = request.args.get("title")
    movie_year = request.args.get("year")
    movie_description = request.args.get("description")
    movie_rating = request.args.get("rating")
    movie_ranking = request.args.get("ranking")
    movie_review = request.args.get("review")
    movie_img_url = request.args.get("img_url")
    db.session.add(
        Movie(
            title=movie_title,
            year=movie_year,
            description=movie_description,
            rating=movie_rating,
            ranking=movie_ranking,
            review=movie_review,
            img_url=movie_img_url,
        )
    )
    db.session.commit()
    return redirect("/")


@app.route("/select", methods=["POST", "GET"])
def select():
    movie_title = request.args.get("movie_title")
    movie_search_params = {"query": movie_title}
    response = requests.get(
        url=movie_search_url, headers=movie_search_headers, params=movie_search_params
    )
    data = response.json()
    print(json.dumps(data, indent=2))
    movie_data = []
    for result in data["results"]:
        movie = {
            "title": result.get("original_title", None),
            "year": result.get("release_date", "Unreleased"),
            "description": result.get("overview", "No Description"),
            "rating": float(result.get("vote_average", 0.0)),
            "ranking": "None",
            "review": "None",
            "img_url": f"https://image.tmdb.org/t/p/w500/{result.get("poster_path", None)}",
        }
        movie_data.append(movie)
    print(movie_data)
    return render_template("select.html", movies=movie_data)


if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
