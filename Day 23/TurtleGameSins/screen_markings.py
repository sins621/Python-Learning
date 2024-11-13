from turtle import Turtle
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class ScreenMarker(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.color("white")

    def draw_screen(self):
        self.goto(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.pd()
        self.goto(SCREEN_WIDTH / -2, SCREEN_HEIGHT / 2)
        self.goto(SCREEN_WIDTH / -2, SCREEN_HEIGHT / -2)
        self.goto(SCREEN_WIDTH / 2, SCREEN_HEIGHT / -2)
        self.goto(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.pu()
