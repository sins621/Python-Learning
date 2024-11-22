from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("./Day 30/Json Project/passwords.json", mode="r") as passwords:
            data = json.load(passwords)
            if website in data:
                mail = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(
                    title=website, message=f"Email: {mail}\nPassword: {password}"
                )
            else:
                messagebox.showerror(
                    title="Error", message=f"{website} Not Found in Database"
                )

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")


def gen_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []
    for char in range(0, nr_letters):
        password_list.append(choice(letters))

    for char in range(0, nr_symbols):
        password_list.append(choice(symbols))

    for char in range(0, nr_numbers):
        password_list.append(choice(numbers))

    shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    mail = mail_user_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": mail, "password": password}}

    if len(website) == 0 or len(mail) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Oops..", message="Please don't leave any fields empty!"
        )
    else:
        try:
            with open("./Day 30/Json Project/passwords.json", mode="r") as passwords:
                data = json.load(passwords)
        except FileNotFoundError:
            with open("./Day 30/Json Project/passwords.json", mode="w") as passwords:
                json.dump(new_data, passwords, indent=4)
        else:
            data.update(new_data)

            with open("./Day 30/Json Project/passwords.json", mode="w") as passwords:
                json.dump(data, passwords, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

wn = Tk()
wn.title("Password Manager")
wn.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./Day 29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Webstite:")
website_label.grid(row=1, column=0)

mail_user_label = Label(text="Email/Username:")
mail_user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=25)
website_entry.focus()
website_entry.grid(row=1, column=1)

mail_user_entry = Entry(width=45)
mail_user_entry.insert(0, "bradlycarpenterza@gmail.com")
mail_user_entry.grid(row=2, column=1, columnspan=2)

gen_pass_button = Button(text="Generate Password", command=gen_password)
gen_pass_button.grid(row=3, column=2)

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

add_pass_button = Button(text="Add", width=42, command=save)
add_pass_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(row=1, column=2)

wn.mainloop()
