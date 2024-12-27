from flask import Flask, render_template
from random import randint
from datetime import datetime
from requests import get

app = Flask(__name__)

time = datetime.now()


@app.route("/")
def home():
    random_number = randint(1, 10)
    year = time.year
    name = "Sins"
    return render_template(
        "index.html", random_number=random_number, year=year, name=name
    )


@app.route("/guess/<name>")
def guess(name):
    params = {"name": name}
    genderize_url = " https://api.genderize.io"
    gender_response = get(url=genderize_url, params=params)
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    agify_url = " https://api.agify.io"
    age_response = get(url=agify_url, params=params)
    age_response.raise_for_status()
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", gender=gender, age=age, name=name.title())


@app.route("/blog/<int:num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    print(num)
    response = get(url=blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
