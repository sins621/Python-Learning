from car import Car
from random import randint
from config import SCREEN_WIDTH, SCREEN_HEIGHT

GRID_DIV_SIZE = 50
OFFSET = 20

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
                    randint(1,10)
                    )
            self.cars.append(new_car)

    def update(self, player):
        self.move()

    def move(self):
        for car in self.cars:
            car.move()
            if car.xcor() < SCREEN_WIDTH//-2 + OFFSET:
                car.goto(
                        SCREEN_WIDTH//2 - OFFSET,
                        car.ycor()
                        )
