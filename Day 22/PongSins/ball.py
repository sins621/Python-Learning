from turtle import Turtle

SPEED = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.setheading(0)

    def hor_collision(self, paddle_ycor, paddle_dis):
        self.setheading((self.heading() - 180) * -1)

        if self.heading() < 90 or self.heading() > 270:
            if self.ycor() > paddle_ycor:
                self.setheading(self.heading() + paddle_dis//4)
            else:
                self.setheading(self.heading() - paddle_dis//4)

        else:
            if self.ycor() > paddle_ycor:
                self.setheading(self.heading() - paddle_dis//4)
            else:
                self.setheading(self.heading() + paddle_dis//4)

    def ver_collision(self):
        pass

