from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from sqlalchemy.exc import SQLAlchemyError
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key-goes-here"

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


def db_has_email(db_object, db_list):
    for db_item in db_list:
        if db_object.email == db_item.email:
            return True
    return False


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         try:
#             data = request.form
#             user_name = data.get("name", "")
#             user_email = data.get("email", "")
#             user_password = generate_password_hash(
#                 data.get("password", ""), method="pbkdf2:sha256", salt_length=16
#             )
#             new_user = User(name=user_name, email=user_email, password=user_password)
#             db.session.add(new_user)
#             db.session.commit()
#             return redirect(url_for("secrets", name=new_user.name))
#         except SQLAlchemyError as e:
#             return f"Database error {e} occured", 500
#
#     return render_template("register.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # If the user made a POST request, create a new user
    if request.method == "POST":
        user = User(
            name=request.form.get("name"),
            password=generate_password_hash(
                request.form.get("password", ""), method="pbkdf2:sha256", salt_length=16
            ),
            email=request.form.get("email"),
        )
        # Add the user to the database
        db.session.add(user)
        # Commit the changes made
        db.session.commit()
        # Once user account created, redirect them
        # to login route (created later on)
        return redirect(url_for("login", name=user.name))
    # Renders sign_up template if user made a GET request
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # If a post request was made, find the user by
    # filtering for the username
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        # Check if the password entered is the
        # same as the user's password
        if user:
            print(user.name, user.password)
            if user.password == generate_password_hash(
                request.form.get("password", ""), method="pbkdf2:sha256", salt_length=16
            ):
                # Use the login_user method to log in the user
                login_user(user)
                return redirect(url_for("secrets"))
        # Redirect the user back to the home
    return render_template("login.html")


@app.route("/secrets")
def secrets():
    return render_template("secrets.html", name=request.args.get("name"))


@app.route("/logout")
def logout():
    return ""


@app.route("/download")
def download():
    print("Accessed Download")
    return send_from_directory(
        directory="static", path="files/cheat_sheet.pdf", as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True, port=5003)
