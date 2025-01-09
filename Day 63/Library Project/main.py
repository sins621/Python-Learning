from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

# TODO: 1. Display DB @ home
# TODO: 2. Add New Books @ add
# TODO: 3. Add <a>Change Rating</a> To Each Element
# TODO: 4. Add <a>Delete</a> To Each Element

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.sqlite3"

db = SQLAlchemy(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating


all_books = []

# with app.app_context():
#     db.create_all()
#     new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

@app.route("/", methods=["GET", "POST"])
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    if request.method == "POST":
        pass
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form
        book_data = Book(
            title=data["book_name"],
            author=data["book_author"],
            rating=data["book_rating"],
        )
        db.session.add(book_data)
        db.session.commit()
        return redirect("/")
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get('book_id', type = int)
    if request.method == "POST":
        data = request.form
        rating = data["rating"]
        book_id = data["book_id"]
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        book_to_update.rating = float(rating)
        db.session.commit()
        return redirect("/")
    else:
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    return render_template("edit.html", id=book_id, book=book_to_update)

if __name__ == "__main__":
    app.run(debug=True)
