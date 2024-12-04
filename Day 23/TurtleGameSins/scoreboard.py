from turtle import Turtle

from config import SCREEN_HEIGHT, SCREEN_WIDTH

FONT = ("Courier", 24, "normal")
Y_OFFSET = 40
X_OFFSET = 10
POSITION = (SCREEN_WIDTH//-2 + X_OFFSET, SCREEN_HEIGHT//2 - Y_OFFSET)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.pu()
        self.ht()
        self.color("white")
        self.goto(POSITION)
        self.write(
                f"LEVEL: {self.level}",
                False,
                align="left",
                font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(
                f"LEVEL: {self.level}",
                False,
                align="left",
                font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(
                "GAME OVER",
                False, 
                align="center",
                font=FONT
                )
