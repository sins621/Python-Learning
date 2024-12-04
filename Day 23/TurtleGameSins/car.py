from random import choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self, x_pos, y_pos, speed):
        super().__init__()
        self.speed = speed
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(choice(COLORS))
        self.pu()
        self.goto(self.x_pos, self.y_pos)

    def move(self):
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())

    def reset_pos(self):
        pass
