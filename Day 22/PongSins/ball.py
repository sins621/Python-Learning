from turtle import Turtle

velocity = 10
direction = [1,0]
COL_ANGLE = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.direction = direction
        self.velocity = velocity

    def move(self):
        new_direction = [i * self.velocity for i in self.direction]
        self.setpos(self.pos() + new_direction)

    def new_round(self):
        self.setpos(0,0)
        self.direction = [-1,0]
        self.velocity = velocity

    def paddle_col(self, seg_num, player_num):
        if player_num == 1:
            self.direction[0] = 1
        if player_num == 2:
            self.direction[0] = -1

        if seg_num == 4:
            self.direction[1] = COL_ANGLE*2
        elif seg_num == 3:
            self.direction[1] = COL_ANGLE
        elif seg_num == 1:
            self.direction[1] = -COL_ANGLE
        elif seg_num == 0:
            self.direction[1] = -COL_ANGLE*2
        else:
            self.direction[1] = 0


    def wall_col(self):
        self.direction[1] *= -1

    def is_out_of_bounds(self):
        pass

