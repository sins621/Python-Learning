from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.ht()
        self.color("white")
        self.goto(0,270)
        self.write(
                f"SCORE: {self.score}", False, align="center",font=('Courier',18,'bold'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(
                f"SCORE: {self.score}",
                False, 
                align="center",font=('Courier',18,'bold')
                )

    def game_over(self):
        self.goto(0,0)
        self.write(
                "GAME OVER",
                False, 
                align="center",font=('Courier',18,'bold')
                )
