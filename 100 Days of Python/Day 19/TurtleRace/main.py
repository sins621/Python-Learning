from random import randint
from turtle import Screen, Turtle

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
GRID_DIVISION = 40
FINISH_LINE_X = (SCREEN_WIDTH/2) - 30
COLORS = ["blue", "red", "green", "yellow", "pink", "cyan"]
turtles = []

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("#282828")

def draw_screen(): 
    pen = Turtle()
    pen.ht()
    pen.color("white")
    pen.pu()
    pen.goto(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    pen.pd()
    pen.goto(SCREEN_WIDTH/-2,SCREEN_HEIGHT/2)
    pen.goto(SCREEN_WIDTH/-2,SCREEN_HEIGHT/-2)
    pen.goto(SCREEN_WIDTH/2,SCREEN_HEIGHT/-2)
    pen.goto(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    pen.pu()

def draw_finishline():
    pen = Turtle()
    pen.ht()
    pen.pu()
    pen.color("red")
    pen.goto(FINISH_LINE_X, SCREEN_HEIGHT/-2+1)
    pen.pd()
    pen.goto(FINISH_LINE_X, SCREEN_HEIGHT/2-1)
    pen.pu()

def turtle_generator(COLORS, turtles, GRID_DIVISION):
    x_pos = ((-1*SCREEN_WIDTH/2)+GRID_DIVISION)
    for i in range(len(COLORS)):
        turtles.append(Turtle())
        turtles[i].color(COLORS[i])
        turtles[i].shape("turtle")
        turtles[i].pu()
        y_pos = ( (-1*SCREEN_HEIGHT/2)+
                (SCREEN_HEIGHT/len(COLORS)*(i)+
                 (SCREEN_HEIGHT/len(COLORS)/2)))
        turtles[i].goto(x_pos, y_pos)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?")
draw_screen()
draw_finishline()
turtle_generator(COLORS, turtles, GRID_DIVISION)

racing = True
winning_turtle = ""
while racing:
    for turtle in turtles:
        turtle.forward(randint(1,10))
        if turtle.xcor() > FINISH_LINE_X-10:
            racing = False
            winning_turtle = turtle.pencolor()
            break

if user_bet == winning_turtle:
    print(f"Congrats, {winning_turtle} won!")
else:
    print(f"Unlucky, {winning_turtle} won.")

screen.mainloop()
screen.done()
