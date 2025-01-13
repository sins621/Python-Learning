from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
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


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


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

        return jsonify(
            cafe={
                "id": random_cafe.id,
                "name": random_cafe.name,
                "map_url": random_cafe.map_url,
                "img_url": random_cafe.img_url,
                "location": random_cafe.location,
                "seats": random_cafe.seats,
                "has_toilet": random_cafe.has_toilet,
                "has_wifi": random_cafe.has_wifi,
                "has_sockets": random_cafe.has_sockets,
                "can_take_calls": random_cafe.can_take_calls,
                "coffee_price": random_cafe.coffee_price,
            }
        )

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

        print(all_cafes)
        cafe_list = []
        for cafe_item in all_cafes:
            cafe = {
                "id": cafe_item.id,
                "name": cafe_item.name,
                "map_url": cafe_item.map_url,
                "img_url": cafe_item.img_url,
                "location": cafe_item.location,
                "seats": cafe_item.seats,
                "has_toilet": cafe_item.has_toilet,
                "has_wifi": cafe_item.has_wifi,
                "has_sockets": cafe_item.has_sockets,
                "can_take_calls": cafe_item.can_take_calls,
                "coffee_price": cafe_item.coffee_price,
            }
            cafe_list.append(cafe)
        return jsonify(cafes=cafe_list)

    except SQLAlchemyError as e:
        print(f"Database query failed: {e}")
        return jsonify({"error": "Database error occurred"}), 500


# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == "__main__":
    app.run(debug=True)
