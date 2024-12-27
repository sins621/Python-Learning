from flask import Flask, render_template
from requests import get


app = Flask(__name__)

all_posts = None


@app.route("/")
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = get(url=blog_url)
    response.raise_for_status()
    global all_posts
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/blog/<int:id>")
def get_post(id):
    global all_posts
    if all_posts != None:
        post = all_posts[id - 1]
        return render_template("post.html", post=post)
    else:
        return "No Post At That Address"


if __name__ == "__main__":
    app.run(debug=True)
