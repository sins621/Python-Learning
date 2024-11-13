#TODO: Fix Reset Bug
from turtle import Screen, Turtle
from layout import Layout
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
layout = Layout(screen)

p1_paddle = Paddle(layout.SCREEN_WIDTH, layout.SCREEN_HEIGHT, 1)
p2_paddle = Paddle(layout.SCREEN_WIDTH, layout.SCREEN_HEIGHT, 2)
ball = Ball()
p1_scoreboard = Scoreboard(layout.SCREEN_WIDTH, layout.SCREEN_HEIGHT, "left")
p2_scoreboard = Scoreboard(layout.SCREEN_WIDTH, layout.SCREEN_HEIGHT, "right")

screen.listen()
screen.onkey(p1_paddle.move_up, "w")
screen.onkey(p1_paddle.move_down, "s")
screen.onkey(p2_paddle.move_up, "i")
screen.onkey(p2_paddle.move_down, "k")


PADDLE_COL_DIS = 20
WALL_COL_DIS = -10
DELTA = 0.016

# Game Loop
is_playing = True
while is_playing:


    for i in range(len(p1_paddle.segments)):
        if p1_paddle.segments[i].distance(ball.pos()) < PADDLE_COL_DIS:
            ball.paddle_col(i,1)

    for i in range(len(p2_paddle.segments)):
        if p2_paddle.segments[i].distance(ball.pos()) < PADDLE_COL_DIS:
            ball.paddle_col(i,2)

    if abs(ball.ycor()) > abs(layout.SCREEN_HEIGHT//2 + WALL_COL_DIS):
        ball.wall_col()

    if ball.xcor() > layout.SCREEN_WIDTH//2:
        ball.new_round()
        p1_paddle.new_round(1)
        p2_paddle.new_round(2)
        p1_scoreboard.increase_score()

    if ball.xcor() < layout.SCREEN_WIDTH//-2:
        ball.new_round()
        p1_paddle.new_round(1)
        p2_paddle.new_round(2)
        p2_scoreboard.increase_score()

    # Update Frame
    ######################################################
    ball.move()
    time.sleep(DELTA)
    screen.update()

screen.exitonclick()

