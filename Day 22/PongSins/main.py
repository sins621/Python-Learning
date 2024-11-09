from turtle import Screen, Turtle
from layout import Layout
from paddle import Paddle
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

# Game Loop
is_running = True
while is_running:
    # Update Frame
    ######################################################
    time.sleep(0.016)
    screen.update()
