from flask import Flask, render_template
import requests


class BlogPost:
    def __init__(self, **kw):
        self.id = kw.get("id")
        self.author = kw.get("author")
        self.date = kw.get("date")
        self.body = kw.get("body")
        self.title = kw.get("title")
        self.subtitle = kw.get("subtitle")
        self.image_url = kw.get("image_url")


response = requests.get(url="https://api.npoint.io/f76b2850b664d1e440b8")
response.raise_for_status()
data = response.json()

blog_posts = []

for item in data:
    blog_post = BlogPost(
        id=item["id"],
        author=item["author"],
        date=item["date"],
        body=item["body"],
        title=item["title"],
        subtitle=item["subtitle"],
        image_url=item["image_url"],
    )
    blog_posts.append(blog_post)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    for blog_post in blog_posts:
        if blog_post.id == post_id:
            return render_template("post.html", blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
