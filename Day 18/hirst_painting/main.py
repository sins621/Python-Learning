###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle as t
from random import choice

import colorgram

t.colormode(255)
pen = t.Turtle()
screen = t.Screen()
screen.bgcolor("white")

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

pen.pu()
pen.speed(0)
pen.hideturtle()

for y in range(17):
    pen.goto(-300,-320 + (y*41))
    for x in range(15):
        pen.dot(20,choice(rgb_colors))
        pen.forward(41)

screen.exitonclick()
