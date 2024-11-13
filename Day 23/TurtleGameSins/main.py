import time
from turtle import Screen
from player import Player
from screen_markings import ScreenMarker
from car_manager import CarManager
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FINISH_POS_OFFSET
from scoreboard import Scoreboard

DELTA = 0.016

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("#282828")
screen.tracer(0)

player = Player()

screen_marker = ScreenMarker()
screen_marker.draw_screen()
screen_marker.draw_finish()

car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    car_manager.move()

    if car_manager.is_collision(player):
        game_is_on = False
        scoreboard.game_over()

    if player.ycor() > SCREEN_HEIGHT // 2 - FINISH_POS_OFFSET:
        scoreboard.increase_level()
        player.goto(0, SCREEN_HEIGHT//-2 + 20)

    time.sleep(DELTA)
    screen.update()

screen.exitonclick()
