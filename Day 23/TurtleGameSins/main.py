import time
from turtle import Screen
from player import Player
from screen_markings import ScreenMarker
from car_manager import CarManager
from config import SCREEN_WIDTH, SCREEN_HEIGHT
#from scoreboard import Scoreboard

DELTA = 0.016

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("#282828")
screen.tracer(0)

player = Player()

screen_marker = ScreenMarker()
screen_marker.draw_screen()

car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    car_manager.update(player)
    time.sleep(DELTA)
    screen.update()
