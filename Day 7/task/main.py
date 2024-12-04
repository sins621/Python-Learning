import os
import platform
import random

import hangman_ascii
import words

clear = lambda: (
    os.system("cls") if platform.system() == "Windows" else os.system("clear")
)
clear()
print(hangman_ascii.HANGMAN_LOGO)

def listToString(list):
    string = ""
    for l in list:
        string += l
    return string


def listContainsUnderscores(list):
    if "_" in list:
        return True
    else:
        return False


def listContainsGuess(list, guess):
    if guess in list:
        return True
    else:
        return False


lives = 6

print(f"Lives remaining: {lives}")
print(hangman_ascii.HANGMAN_PICS[-lives - 1])

chosen_word = random.choice(words.WORD_LIST)

display = list("_" * len(chosen_word))
print(listToString(display))

while listContainsUnderscores(display) and lives != 0:
    guess = input("Guess a letter: \n")
    clear()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            print(f"You guessed correctly, {guess} is a letter in the word")

    if not listContainsGuess(display, guess):
        lives -= 1
        print(f"You guessed incorrectly, {guess} is not a letter in the word")

    print(f"Lives remaining: {lives}")
    print(hangman_ascii.HANGMAN_PICS[-lives - 1])
    print(listToString(display))
    if lives == 0:
        print("You lose")
    if not listContainsUnderscores(display):
        print("You win")
