from turtle import Turtle, Screen
from snake import Snake
from food import Food
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
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_DIVISION)
food.create_food()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

while is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
