from turtle import Turtle
import config

STARTING_OFFSET = 20
SPEED = 10

class Player(Turtle):
    def __init__(self):
        self.starting_position = (0, -280)
        self.move_distance = 10
        self.finish_line_y = 280
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto(self.starting_position)
        self.setheading(90)
        self.goto(0, config.SCREEN_HEIGHT//-2 + STARTING_OFFSET)

    def move(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)
