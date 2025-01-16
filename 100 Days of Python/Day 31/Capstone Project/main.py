from random import randint
from tkinter import *
from tkinter import messagebox

import pandas

BACKGROUND_COLOR = "#B1DDC6"
PATH = "./Day 31/Capstone Project/"
DELAY_SEC = 3
index = None

try:
    try:
        word_data = pandas.read_csv(f"{PATH}/data/words_to_learn.csv")
        word_dict = word_data.to_dict(orient="list")
    except:
        word_data = pandas.read_csv(f"{PATH}/data/french_words.csv")
        word_dict = word_data.to_dict(orient="list")
except FileNotFoundError as error:
    messagebox.showerror(title="No File", message="Word Database Not Found")


def next_card():
    global index

    if len(word_dict["French"]) == 0:
        messagebox.showinfo(title="Word Error", message="You've run out of words")
    else:
        index = randint(0, len(word_dict["French"]) - 1)
        french_word = word_dict["French"][index]
        canvas.itemconfig(word_text, text=french_word, fill="black")
        canvas.itemconfig(lang_text, text="French", fill="black")
        canvas.itemconfig(canvas_image, image=front_image)
        count_down(3)


def flip_card():
    english_word = word_dict["English"][index]
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(word_text, text=english_word, fill="white")
    canvas.itemconfig(lang_text, text="English", fill="white")


def count_down(count):
    if count > 0:
        wn.after(1000, count_down, count - 1)
    else:
        flip_card()


def is_known():
    if index is not None:
        del word_dict["French"][index], word_dict["English"][index]
        word_data = pandas.DataFrame.from_dict(word_dict)
        word_data.to_csv(f"{PATH}/data/words_to_learn.csv", mode="w", index=False)

    next_card()


wn = Tk()
wn.title("Flashy")
wn.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
front_image = PhotoImage(file=f"{PATH}/images/card_front.png")
back_image = PhotoImage(file=f"{PATH}/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
lang_text = canvas.create_text(400, 150, text="test", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="test", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file=f"{PATH}/images/wrong.png")
no_button = Button(
    image=wrong_image,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    bd=0,
    command=next_card,
)
no_button.grid(row=1, column=0)

right_image = PhotoImage(file=f"{PATH}/images/right.png")
yes_button = Button(
    image=right_image,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    bd=0,
    command=is_known,
)
yes_button.grid(row=1, column=1)

next_card()

wn.mainloop()
