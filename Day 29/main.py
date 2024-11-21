from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2)

mail_user_entry = Entry(width=45)
mail_user_entry.grid(row=2, column=1, columnspan=2)

gen_pass_button = Button(text="Generate Password")
gen_pass_button.grid(row=3, column=2)

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

add_pass_button = Button(text="Add", width=42)
add_pass_button.grid(row=4, column=1, columnspan=2)


wn.mainloop()
