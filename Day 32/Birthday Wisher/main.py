import pandas
import datetime as dt
from random import randint, choice

birthday_dict = None

PATH = "./Day 32/Birthday Wisher/"

try:
    birthday_data = pandas.read_csv(f"{PATH}/birthdays.csv")
except:
    print("FileNotFound")
else:
    birthday_dict = birthday_data.to_dict(orient="records")

rand_letter_num = randint(1, 3)
letter_path = f"{PATH}letter_templates/letter_{rand_letter_num}.txt"

try:
    with open(letter_path) as letter_file:
        letter = letter_file.readlines()
except:
    print("Letter not Found")

# for name in names:
#     new_string = ""
#     new_name = name.strip()
#     for line in contents:
#         new_line = line.replace("[name]", f"{new_name}")
#         new_string += new_line
#     with open(f"./Output/ReadyToSend/{new_name}.txt", mode="w") as new_letter:
#         new_letter.write(new_string)

# Dicitonary Structure
# new_dict = [
#     {
#         "name": "yahoo",
#         "email": "fl0586114@gmail.com",
#         "year": 1961,
#         "month": 11,
#         "day": 23,
#     },
#     {
#         "name": "bradgmail",
#         "email": "bradlycarpenterza@gmail.com",
#         "year": 1961,
#         "month": 11,
#         "day": 23,
#     },
# ]

now = dt.datetime.now()
day_of_week = now.weekday()
