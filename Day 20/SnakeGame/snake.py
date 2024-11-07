from turtle import Turtle
from random import randint

class Snake:
    def __init__(self):
        self.body = []
        self.gen_snake()
        self.head = self.body[0]

    def random_hex(self):
        hex = "#"
        for i in range(6):
            hex += str(randint(0,9))
        return hex

    def gen_snake(self):
        for i in range(6):
            square = Turtle(shape="square")
            square.pu()
            square.color(self.random_hex())
            if len(self.body) == 0:
                pass
            else:
                square.setx(self.body[i-1].xcor() - 20)
            self.body.append(square)

    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            new_x = self.body[i-1].xcor()
            new_y = self.body[i-1].ycor()
            self.body[i].goto(new_x,new_y)
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
