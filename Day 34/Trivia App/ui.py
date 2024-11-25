import tkinter as Tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
PADDING = 20
PATH = "./Day 34/Trivia App"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=PADDING, pady=PADDING, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Tk.Label(text=f"Score: {self.score}")
        self.score_label.config(bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Tk.Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=PADDING)
        self.question_text = self.canvas.create_text(
            150, 125, text="Placeholder", font=FONT, width=280
        )

        false_image = Tk.PhotoImage(file=f"{PATH}/images/false.png")
        self.false_button = Tk.Button(
            image=false_image,
            bg=THEME_COLOR,
            highlightthickness=0,
            bd=0,
            command=self.false_pressed,
        )
        self.false_button.grid(row=2, column=0)

        true_image = Tk.PhotoImage(file=f"{PATH}/images/true.png")
        self.true_button = Tk.Button(
            image=true_image,
            bg=THEME_COLOR,
            highlightthickness=0,
            bd=0,
            command=self.true_pressed,
        )
        self.true_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def true_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def get_next_question(self):
        q_text = self.quiz_brain.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=q_text)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        pass
