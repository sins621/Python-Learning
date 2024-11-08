from turtle import Turtle
from random import choice

class Food:
    def __init__(
        self,
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        GRID_DIVISION,
    ):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.GRID_DIVISION = GRID_DIVISION
        self.x_cords = []
        self.y_cords = []
        self.create_grid()

    def create_food(self):
        food = Turtle(shape="square")
        food.pu()
        food.color("white")
        food.goto(choice(self.x_cords), choice(self.y_cords))

    def create_grid(self):
        x_divisions = int(self.SCREEN_WIDTH/self.GRID_DIVISION)
        y_divisions = int(self.SCREEN_HEIGHT/self.GRID_DIVISION)

        for i in range(x_divisions):
            self.x_cords.append(i*self.GRID_DIVISION)
        for i in range(y_divisions):
            self.y_cords.append(i*self.GRID_DIVISION)
