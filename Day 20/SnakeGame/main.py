from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_DIVISION = 20
LOSE_PADDING = 0
LOSE_WIDTH = SCREEN_WIDTH//2 - LOSE_PADDING
LOSE_HEIGHT = SCREEN_HEIGHT//2 - LOSE_PADDING

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
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

while is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > LOSE_WIDTH or snake.head.xcor() < LOSE_WIDTH * -1 or snake.head.ycor() > LOSE_HEIGHT or snake.head.ycor() < LOSE_HEIGHT * -1:
        is_running = False
        scoreboard.game_over()

    for square in snake.body[1:]:
        if snake.head.distance(square) < 10:
            is_running = False
            scoreboard.game_over()

screen.exitonclick()
