from random import choice
from turtle import Screen, Turtle

from colors import turtle_colors

turtle = Turtle()
screen = Screen()
SHAPES = 10
DISTANCE = 100
MIN_SIDES = 3

screen.bgcolor("black")
# I'm the best
for num_sides in range(MIN_SIDES,SHAPES + 1):
    turtle.color(choice(turtle_colors))
    angle = 360/num_sides
    for j in range(num_sides):
        turtle.forward(DISTANCE)
        turtle.right(angle)

screen.exitonclick()
