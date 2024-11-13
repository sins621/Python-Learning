from car import Car
from random import randint
from config import SCREEN_WIDTH, SCREEN_HEIGHT

GRID_DIV_SIZE = 50
OFFSET = 20
COL_OFFSET = 28
COL_DIS = 30
PLAYER_OFFSET = 10
MIN_SPEED = 1
MAX_SPEED = 5

class CarManager:
    def __init__(self):
        self.y_positions = SCREEN_HEIGHT//GRID_DIV_SIZE - 3
        self.cars = []

        for i in range(self.y_positions):
            y_min = SCREEN_HEIGHT//-2
            new_car = Car(
                    randint(
                        SCREEN_WIDTH//-2 + OFFSET,
                        SCREEN_WIDTH//2 - OFFSET),
                    y_min + GRID_DIV_SIZE * (i+2),
                    randint(MIN_SPEED,MAX_SPEED)
                    )

            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.move()
            if car.xcor() < SCREEN_WIDTH//-2 + OFFSET:
                car.goto(
                        SCREEN_WIDTH//2 - OFFSET,
                        car.ycor()
                        )

    def is_collision(self, player):
        for car in self.cars:
            if player.ycor() > car.ycor() - COL_OFFSET:
                if car.distance(player) < COL_DIS:
                    if player.ycor() + PLAYER_OFFSET < car.ycor() + COL_OFFSET:
                        return True

        return False
