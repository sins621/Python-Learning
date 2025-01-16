import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_lable = tkinter.Label(text="I am a label", font=("Arial", 24))
my_lable.pack(expand=True)

window.mainloop()
