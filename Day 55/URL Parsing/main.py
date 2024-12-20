from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Cool Heading</h1>" \
        "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjdiZ24waDhxdmZndjc3czFwczY2c255eDI2MXRrMGd6YWVsOWFhMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YHYmMLkOmqoo/giphy.gif' style='margin-left: 25%'>"

@app.route("/bye")
def bye():
    return "Bye"

@app.route("/<user>")
def greet(user):
    return f"Hello {user + 5}"

if __name__ == "__main__":
    app.run(debug=True)
