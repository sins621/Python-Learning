import csv

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, url

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField("Cafe Name", validators=[DataRequired()])
    cafe_location = StringField(
        "Cafe Location On Google Maps (URL)", validators=[DataRequired(), url()]
    )
    cafe_opening_time = StringField(
        "Cafe Opening Time e.g. 8AM", validators=[DataRequired()]
    )
    cafe_closing_time = StringField(
        "Cafe Closing Time e.g. 5:30PM", validators=[DataRequired()]
    )
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=[
            ("☕️"),
            ("☕️☕️"),
            ("☕️☕️☕️"),
            ("☕️☕️☕️☕️"),
            ("☕️☕️☕️☕️☕️"),
        ],
        validators=[DataRequired()],
    )
    wifi_rating = SelectField(
        "Wifi Strength Rating",
        choices=[
            ("✘"),
            ("💪"),
            ("💪💪"),
            ("💪💪💪"),
            ("💪💪💪💪"),
            ("💪💪💪💪💪"),
        ],
        validators=[DataRequired()],
    )
    power_rating = SelectField(
        "Power Socket Availability",
        choices=[
            ("✘"),
            ("🔌"),
            ("🔌🔌"),
            ("🔌🔌🔌"),
            ("🔌🔌🔌🔌"),
            ("🔌🔌🔌🔌🔌"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        fields = [
            form.cafe_name.data,
            form.cafe_location.data,
            form.cafe_opening_time.data,
            form.cafe_closing_time.data,
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.power_rating.data,
        ]
        with open("cafe-data.csv", mode="a", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fields)
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
