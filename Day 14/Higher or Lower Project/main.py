import os
import platform
import random

import art
import game_data
from game_data import data

clear = lambda: (
    os.system("cls") if platform.system() == "Windows" else os.system("clear")
)


def print_option(dict, AorB):
    print(
        f"Compare {AorB}: {dict["name"]}, a {dict["description"]}, from "
        f"{dict["country"]}."
    )


print(art.logo)

score = 0
option1 = random.choice(data)
option2 = random.choice(data)
choice = 0
game_over = "n"

while game_over == "n":
    print_option(option1, "A")
    print(art.vs)
    print_option(option2, "B")
    choice = input("Who has more followers? Type 'A' or 'B': \n").lower()

    if choice == "a":
        if option1["follower_count"] > option2["follower_count"]:
            score += 1
            clear()
            print(art.logo)
            print(f"You're right! Current score: {score}.")
            option2 = random.choice(data)
            if option1 == option2:
                option2 = random.choice(data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = "y"
    
    if choice == "b":
        if option2["follower_count"] > option1["follower_count"]:
            score += 1
            clear()
            print(art.logo)
            print(f"You're right! Current score: {score}.")
            option1 = option2
            option2 = random.choice(data)
            if option1 == option2:
                option2 = random.choice(data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = "y"
