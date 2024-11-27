import pandas
import datetime as dt
import smtplib

from random import randint

PATH = "./Day 32/Birthday Wisher/"

my_email = "fl0586114@gmail.com"
my_password = ""

def send_birthday_message(mail, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=mail,
            msg=f"Subject:Happy Birthday\n\n{message}",
        )


try:
    birthday_data = pandas.read_csv(f"{PATH}/birthdays.csv")
except:
    print("Birthday Database Not Found")
else:
    birthday_list = birthday_data.to_dict(orient="records")

rand_letter_num = randint(1, 3)
letter_path = f"{PATH}letter_templates/letter_{rand_letter_num}.txt"

try:
    with open(letter_path) as letter_file:
        letter = letter_file.readlines()
except:
    print("Letters Not Found")

now = dt.datetime.now()
current_month = now.month
current_day = now.day

for contact in birthday_list:
    if current_month == contact["month"] and current_day == contact["day"]:
        final_letter = ""
        for line in letter:
            new_line = line.replace("[NAME]", f"{contact["name"]}")
            final_letter += new_line
    send_birthday_message(contact["email"], final_letter)
