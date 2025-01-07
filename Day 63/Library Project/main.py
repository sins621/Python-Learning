from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route("/")
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form
        book_data = {
            "title": data["book_name"],
            "author": data["book_author"],
            "rating": data["book_rating"],
        }
        all_books.append(book_data)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
