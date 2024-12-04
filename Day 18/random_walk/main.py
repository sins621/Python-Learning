import turtle as t
from random import choice, randint

from colors import turtle_colors

t.colormode(255)
turtle = t.Turtle()
screen = t.Screen()
screen.bgcolor("black")
turtle.color("white")
# I'm the best

distance = 0
direction = randint(0,1)
angle = [0, 90, 180, 270, 360]
turtle.pensize(10)
STROKE_MIN = 10
STROKE_MAX = 100

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r,g,b)
    return random_color

while True:
    turtle.speed(randint(1,3))
    turtle.color(random_color())
    turtle.setheading(choice(angle))
    turtle.forward(randint(STROKE_MIN, STROKE_MAX))

screen.exitonclick()
