from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.sqlite3"

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating


with app.app_context():
    db.create_all()
    new_book = Book(title="masepoes Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
