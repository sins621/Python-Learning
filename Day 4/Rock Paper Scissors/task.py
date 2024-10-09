import random
import os

clear = lambda: os.system("clear")
clear()

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

possibilities = [rock, paper, scissors]

player_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    )
)

if player_choice < len(possibilities):
    print(possibilities[player_choice])
else:
    print("Sorry, that's an invalid option")

cpu_choice = random.randint(0, len(possibilities) - 1)

print(f"Computer chose: \n{possibilities[cpu_choice]}")

if player_choice == cpu_choice:
    print("It's a draw")

elif player_choice == 0 and cpu_choice == 1:
    print("You lose")
elif player_choice == 0 and cpu_choice == 2:
    print("You win")

elif player_choice == 1 and cpu_choice == 0:
    print("You win")
elif player_choice == 1 and cpu_choice == 2:
    print("You lose")

elif player_choice == 2 and cpu_choice == 0:
    print("You lose")
elif player_choice == 2 and cpu_choice == 1:
    print("You win")
