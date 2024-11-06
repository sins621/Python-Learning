from turtle import Turtle, Screen

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
GRID_DIVISION = 40
COLORS = ["blue", "red", "green", "yellow", "pink"]
turtles = []

def turtle_generator(COLORS, turtles, GRID_DIVISION):
    x_pos = ((-1*SCREEN_WIDTH/2)+GRID_DIVISION)
    for i in range(len(COLORS)):
        turtles.append(Turtle())
        turtles[i].color(COLORS[i])
        turtles[i].shape("turtle")
        turtles[i].pu()
        y_pos = ((-1*SCREEN_HEIGHT/2)/GRID_DIVISION+(GRID_DIVISION*i))
        turtles[i].goto(x_pos, y_pos)

turtle_generator(COLORS, turtles, GRID_DIVISION)

screen.mainloop()
