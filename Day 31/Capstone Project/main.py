from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
PATH = "./Day 31/Capstone Project/"


wn = Tk()
wn.title("Flashy")
wn.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
front_image = PhotoImage(file=f"{PATH}/images/card_front.png")
canvas.create_image(400, 263, image=front_image)
lang_text = canvas.create_text(400, 150, text="test", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="test", font=("Ariel", 60, "bold"))

no_button = Button()
no_button.grid(row=1, column = 0)

wn.mainloop()
