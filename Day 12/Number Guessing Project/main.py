import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10
random_number = random.randint(1, 100)
print(f"The number is: {random_number}")
choice = "none"

while choice != "easy" and choice != "hard":
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == "easy":
        attempts = EASY_ATTEMPTS
    elif choice == "hard":
        attempts = HARD_ATTEMPTS
    else:
        print("Incorrect choice")

while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == random_number:
        print(f"You guessed correct! The number is {random_number}")
        break
    elif guess < random_number:
        print("Too low.")
        attempts -= 1
    else:
        print("Too high.")
        attempts -= 1

if attempts == 0:
    print("You've run out of guess, you lose.")
