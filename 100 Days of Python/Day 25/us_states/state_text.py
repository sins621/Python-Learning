from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")


class StateText(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def write_state(self, state_name, position):
        self.goto(position)
        self.write(
            state_name,
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=("Courier", 22, "normal"))
