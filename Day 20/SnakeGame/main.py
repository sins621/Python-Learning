from turtle import Turtle, Screen
from random import random,randint
from snake import Snake
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_DIVISION = 20
squares = []
is_running = True

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("#282828")
screen.title("Snake")
screen.tracer(0)

def draw_screen(): 
    pen = Turtle()
    pen.ht()
    pen.color("white")
    pen.pu()
    pen.goto(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    pen.pd()
    pen.goto(SCREEN_WIDTH/-2,SCREEN_HEIGHT/2)
    pen.goto(SCREEN_WIDTH/-2,SCREEN_HEIGHT/-2)
    pen.goto(SCREEN_WIDTH/2,SCREEN_HEIGHT/-2)
    pen.goto(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    pen.pu()


#############################################################################

draw_screen()

snake = Snake()
screen.listen()
screen.onkey(snake.up,"k")
screen.onkey(snake.down,"j")
screen.onkey(snake.left,"h")
screen.onkey(snake.right,"l")

while is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
