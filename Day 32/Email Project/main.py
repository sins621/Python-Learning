import smtplib
import datetime as dt
from random import choice

PATH = "./Day 32/Email Project"

with open(f"{PATH}/quotes.txt") as quote_file:
    quotes = quote_file.readlines()
    quote = choice(quotes)

my_email = "fl0586114@gmail.com"
my_password = "rukunkpiyccilgxw"


def send_quote(quote):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="blah5115@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}",
        )


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == now.weekday():
    send_quote(quote)
