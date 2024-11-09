from turtle import Screen, Turtle
from layout import Layout
from paddle import Paddle
import time

screen = Screen()
layout = Layout(screen)

p1_paddle = Paddle()

# Game Loop
is_running = True
while is_running:
    # Update Frame
    #######################################################
    time.sleep(0.1)
    screen.update()
