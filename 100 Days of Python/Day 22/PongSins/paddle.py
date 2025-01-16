from turtle import Turtle

#TODO: Clamping Y Axis

PADDLE_LENGTH = 1
PADDLE_WIDTH = 3
OFFSET = 20
SPEED = 20
Y_POSITIONS = [-20,-10, 0, 10, 20]

class Paddle():
    def __init__(self,SCREEN_WIDTH, SCREEN_HEIGHT, player_num):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.segments = []

        if player_num == 1:
            for y_pos in Y_POSITIONS:
                self.add_segment(y_pos, 1)
        elif player_num == 2:
            for y_pos in Y_POSITIONS:
                self.add_segment(y_pos, 2)

    def new_round(self, player_num):
        if player_num == 1:
            for i in range(len(Y_POSITIONS)):
                self.segments[i].goto((self.SCREEN_WIDTH//-2) + OFFSET, Y_POSITIONS[i])
        elif player_num == 2:
            for i in range(len(Y_POSITIONS)):
                self.segments[i].goto((self.SCREEN_WIDTH//2) - OFFSET, Y_POSITIONS[i])


    def add_segment(self, y_pos, player):
        segment = Turtle(shape="square")
        segment.pu()
        segment.color("white")

        if player == 1:
            segment.goto((self.SCREEN_WIDTH//-2) + OFFSET, y_pos)
        else:
            segment.goto((self.SCREEN_WIDTH//2) - OFFSET, y_pos)

        self.segments.append(segment)

    def move_up(self):
        if abs(self.segments[-1].ycor()) < abs(self.SCREEN_HEIGHT//2 - OFFSET):
            for segment in self.segments:
                segment.setheading(90)
                segment.forward(SPEED)

    def move_down(self):
        if abs(self.segments[0].ycor()) < abs(self.SCREEN_HEIGHT//2 - OFFSET):
            for segment in self.segments:
                segment.setheading(270)
                segment.forward(SPEED)
