from turtle import Turtle

PADDING = 30

class Scoreboard(Turtle):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, align):
        super().__init__()
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.align = align
        self.score = 0
        self.pu()
        self.ht()
        self.color("white")

        if self.align == "right":
            self.goto(SCREEN_WIDTH//20 ,SCREEN_HEIGHT//2 - PADDING)
        elif self.align == "left":
            self.goto(SCREEN_WIDTH//-20 ,SCREEN_HEIGHT//2 - PADDING)

        self.write(
                f"{self.score}", False, align="center",font=('Courier',18,'bold'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(
                f"{self.score}", False, align="center",font=('Courier',18,'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write(
                "GAME OVER",
                False, 
                align="center",font=('Courier',18,'bold')
                )
