from turtle import Screen, Turtle
from layout import Layout
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
layout = Layout(screen)
p1_paddle = Paddle(layout.SCREEN_WIDTH, layout.SCREEN_HEIGHT,1)
p2_paddle = Paddle(layout.SCREEN_WIDTH, layout.SCREEN_HEIGHT,2)
screen.listen()

screen.onkey(p1_paddle.move_up, "w")
screen.onkey(p1_paddle.move_down, "s")
screen.onkey(p2_paddle.move_up, "i")
screen.onkey(p2_paddle.move_down, "k")

ball = Ball()

COLLISION_DISTANCE = 35

# Game Loop
is_running = True
while is_running:
    ball.forward(10)

    p1_paddle.sety(ball.ycor())
    p2_paddle.sety(ball.ycor())

    if ball.distance(p1_paddle) < COLLISION_DISTANCE:
        ball.hor_collision(p1_paddle.ycor(), ball.distance(p1_paddle))

    if ball.distance(p2_paddle) < COLLISION_DISTANCE:
        ball.hor_collision(p2_paddle.ycor(), ball.distance(p2_paddle))

    if ball.ycor() > layout.SCREEN_HEIGHT//2:
        ball.ver_collision()

    if ball.ycor() < layout.SCREEN_HEIGHT//-2:
        ball.ver_collision()

    print(ball.pos())

    # Update Frame
    ######################################################
    time.sleep(0.016)
    screen.update()
