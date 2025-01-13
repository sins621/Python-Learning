import json
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafe(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(250), unique=True, nullable=False)
    map_url = mapped_column(String(500), nullable=False)
    img_url = mapped_column(String(500), nullable=False)
    location = mapped_column(String(250), nullable=False)
    seats = mapped_column(String(250), nullable=False)
    has_toilet = mapped_column(Boolean, nullable=False)
    has_wifi = mapped_column(Boolean, nullable=False)
    has_sockets = mapped_column(Boolean, nullable=False)
    can_take_calls = mapped_column(Boolean, nullable=False)
    coffee_price = mapped_column(String(250), nullable=True)

    def __init__(
        self,
        name,
        map_url,
        img_url,
        location,
        seats,
        has_toilet,
        has_wifi,
        has_sockets,
        can_take_calls,
        coffee_price,
    ):
        self.name = name
        self.map_url = map_url
        self.img_url = img_url
        self.location = location
        self.seats = seats
        self.has_toilet = has_toilet
        self.has_wifi = has_wifi
        self.has_sockets = has_sockets
        self.can_take_calls = can_take_calls
        self.coffee_price = coffee_price


with app.app_context():
    db.create_all()


def transform_cafe_o(cafe_o) -> dict:
    return {
        "id": cafe_o.id,
        "name": cafe_o.name,
        "map_url": cafe_o.map_url,
        "img_url": cafe_o.img_url,
        "location": cafe_o.location,
        "seats": cafe_o.seats,
        "has_toilet": cafe_o.has_toilet,
        "has_wifi": cafe_o.has_wifi,
        "has_sockets": cafe_o.has_sockets,
        "can_take_calls": cafe_o.can_take_calls,
        "coffee_price": cafe_o.coffee_price,
    }


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random():
    try:
        result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
        all_cafes = result.scalars().all()
        if not all_cafes:
            return jsonify({"error": "No cafes found"}), 404

        random_cafe = choice(all_cafes)

        return jsonify(transform_cafe_o(random_cafe))

    except SQLAlchemyError as e:
        print(f"Database query failed: {e}")
        return jsonify({"error": "Database error occurred"}), 500


@app.route("/all", methods=["GET"])
def all():
    try:
        result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
        all_cafes = result.scalars().all()
        if not all_cafes:
            return jsonify({"error": "No cafes found"}), 404

        cafe_list = []
        for cafe_item in all_cafes:
            cafe = transform_cafe_o(cafe_item)
            cafe_list.append(cafe)
        return jsonify(cafes=cafe_list)

    except SQLAlchemyError as e:
        print(f"Database query failed: {e}")
        return jsonify({"error": "Database error occurred"}), 500


@app.route("/search")
def search():
    try:
        cafe_location = request.args.get("loc")
        cafe_location_query = db.session.execute(
            db.select(Cafe).where(Cafe.location == cafe_location)
        ).scalar()
        if not cafe_location_query:
            return (
                jsonify({"error": "Sorry, we don't have a cafe at that location."}),
                404,
            )
        return jsonify(cafe=transform_cafe_o(cafe_location_query))
    except SQLAlchemyError as e:
        print(f"Database query failed: {e}")
        return jsonify({"error": "Database error occurred"}), 500


@app.route("/add_cafe", methods=["POST"])
def add_cafe():
    new_cafe_info = request.args
    new_cafe = Cafe(
        name=new_cafe_info.get("name", ""),
        map_url=new_cafe_info.get("map_url", ""),
        img_url=new_cafe_info.get("img_url", ""),
        location=new_cafe_info.get("location", ""),
        seats=new_cafe_info.get("seats", ""),
        has_toilet=new_cafe_info.get("has_toilet", "False").lower() in ["true", "1"],
        has_wifi=new_cafe_info.get("has_wifi", "False").lower() in ["true", "1"],
        has_sockets=new_cafe_info.get("has_sockets", "False").lower() in ["true", "1"],
        can_take_calls=new_cafe_info.get("can_take_calls", "False").lower()
        in ["true", "1"],
        coffee_price=new_cafe_info.get("coffee_price", ""),
    )

    print(json.dumps(transform_cafe_o(new_cafe), indent=2))
    return f"{jsonify(cafe = transform_cafe_o(new_cafe))}"


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == "__main__":
    app.run(debug=True)
