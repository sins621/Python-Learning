import tkinter as tk

window = tk.Tk()

window.title("My First GUI Program")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

label = tk.Label(text="I am a label", font=("Arial", 24, "normal"))
label.grid(column=0, row=0)


def button_clicked():
    text = input.get()
    label.config(text=text)


button = tk.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


button2 = tk.Button(text="Click me", command=button_clicked)
button2.grid(column=2, row=0)

input = tk.Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
