import turtle as t
from random import randint

t.colormode(255)
turtle = t.Turtle()
screen = t.Screen()
screen.bgcolor(40,40,40)
turtle.color("white")
# I'm the best

RADIUS = 150
ANGLE = 2

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r,g,b)
    return random_color

turtle.speed(0)

for _ in range(int(360/ANGLE)):
    turtle.color(random_color())
    turtle.circle(RADIUS)
    turtle.right(ANGLE)

screen.exitonclick()
