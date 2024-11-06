from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

MOVE_SPEED = 10
TURN_SPEED = 20

def move_forward():
    tim.forward(MOVE_SPEED)

def move_backward():
    tim.backward(MOVE_SPEED)

def move_left():
    tim.left(TURN_SPEED)

def move_right():
    tim.right(TURN_SPEED)

def undo():
    tim.undo()

def reset():
    tim.reset()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(undo,"u")
screen.onkey(reset,"c")

screen.mainloop()
