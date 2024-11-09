from turtle import Turtle
from random import randint

STARTING_LENGTH = 6
positions = [(0, 0)]


class Snake:
    def __init__(self):
        self.body = []
        self.gen_snake()
        self.head = self.body[0]

    def random_hex(self):
        hex = "#"
        for i in range(6):
            hex += str(randint(0, 9))
        return hex

    def gen_snake(self):
        for i in range(STARTING_LENGTH - 1):
            positions.append((-20, 0))

        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle(shape="square")
        square.pu()
        square.color(self.random_hex())
        square.goto(position)
        self.body.append(square)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
