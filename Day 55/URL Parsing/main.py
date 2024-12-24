from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route("/")
def hello_world():
    return (
        "<h1 style='text-align: center'>Cool Heading</h1>"
        "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjdiZ24waDhxdmZndjc3czFwczY2c255eDI2MXRrMGd6YWVsOWFhMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YHYmMLkOmqoo/giphy.gif' style='margin-left: 25%'>"
    )


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye"


@app.route("/<user>")
def greet(user):
    return f"Hello {user}"


if __name__ == "__main__":
    app.run(debug=True)
