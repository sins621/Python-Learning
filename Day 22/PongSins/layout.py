from turtle import Turtle, Screen

screen_dimensions = {"small": (640, 480), "medium": (960, 960)}
SCREEN_WIDTH, SCREEN_HEIGHT = screen_dimensions["small"]

LINE_AMOUNT = 10


class Layout(Turtle):
    def __init__(self, screen: Screen):
        super().__init__()
        self.screen = screen
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = screen_dimensions["small"]
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.ht()
        self.color("white")
        self.pu()
        self.goto(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.pd()
        self.goto(SCREEN_WIDTH / -2, SCREEN_HEIGHT / 2)
        self.goto(SCREEN_WIDTH / -2, SCREEN_HEIGHT / -2)
        self.goto(SCREEN_WIDTH / 2, SCREEN_HEIGHT / -2)
        self.goto(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.pu()
        self.goto(0, (SCREEN_HEIGHT / -2) + (SCREEN_HEIGHT // (LINE_AMOUNT * 4)))
        for _ in range(LINE_AMOUNT):
            self.setheading(90)
            self.pd()
            self.forward(SCREEN_HEIGHT // (LINE_AMOUNT * 2))
            self.pu()
            self.forward(SCREEN_HEIGHT // (LINE_AMOUNT * 2))
