from turtle import Turtle

PADDLE_LENGTH = 1
PADDLE_WIDTH = 3
OFFSET = 20
SPEED = 20


class Paddle(Turtle):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, player_num):
        super().__init__()
        self.pu()
        self.color("white")
        self.shape("square")
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.shapesize(PADDLE_LENGTH, PADDLE_WIDTH)
        self.setheading(90)

        if player_num == 1:
            self.goto((SCREEN_WIDTH // -2) + (SCREEN_WIDTH // OFFSET), 0)
        elif player_num == 2:
            self.goto((SCREEN_WIDTH // 2) - (SCREEN_WIDTH // OFFSET), 0)

    def move_up(self):
        if self.ycor() < (self.SCREEN_HEIGHT // 2) - OFFSET*2:
            self.setheading(90)
            self.forward(SPEED)

    def move_down(self):
        if self.ycor() > (self.SCREEN_HEIGHT // -2) + OFFSET*2:
            self.setheading(270)
            self.forward(SPEED)
