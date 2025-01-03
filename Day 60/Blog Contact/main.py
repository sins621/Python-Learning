import os
import smtplib

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

BOT_MAIL_ADDRESS = "fl0586114@gmail.com"
MAIL_PASSWORD = os.getenv("MAIL")


def send_mail(subject, body, to_address):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=BOT_MAIL_ADDRESS, password=MAIL_PASSWORD)
        connection.sendmail(
            from_addr=BOT_MAIL_ADDRESS,
            to_addrs=to_address,
            msg=f"Subject:{subject}\n\n{body}",
        )


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_mail(
            subject=f"Mail from Blog From {data['name']}",
            body=f"""Name: {data["name"]}
Mail: {data["email"]}
Phone: {data["phone"]}
Message: {data["message"]}""",
            to_address="sinsmailza@gmail.com",
        )
        return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
