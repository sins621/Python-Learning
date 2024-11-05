###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t

t.colormode(255)
turtle = t.Turtle()
screen = t.Screen()
screen.bgcolor("black")
turtle.color("white")

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

screen.exitonclick()
