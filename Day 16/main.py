#from turtle import Turtle, Screen

#my_screen = Screen()
#my_screen.bgcolor("black")
#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color("red")
#timmy.forward(100)
#
#print(my_screen.canvheight)
#print(my_screen.canvwidth)
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column(
    "Pokemon Name",
        [
        "Pikachu",
        "Squirtle",
        "Charmander"
        ]
    )

table.add_column(
    "Type",
        [
        "Electric", 
        "Water", 
        "Fire"
        ]
    )

table.align["Pokemon Name"] = "l"
table.align["Type"] = "l"

print(table)
