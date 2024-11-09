from turtle import Turtle

PADDLE_LENGTH = 3
PADDLE_WIDTH = 1

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.shape("square")
        self.shapesize(PADDLE_LENGTH, PADDLE_WIDTH)
        self.goto(0,0)
