from turtle import Turtle, Screen
from colors import turtle_colors
from random import choice

turtle = Turtle()
screen = Screen()
shapes = 10

screen.bgcolor("black")
# I'm the best
for i in range(3,shapes + 1):
    turtle.color(choice(turtle_colors))
    for j in range(i):
        turtle.forward(100)
        turtle.right(360/i)

screen.exitonclick()
