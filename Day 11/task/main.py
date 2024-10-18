# Black Jack Project Bradly Carpenter
# Rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import os
import platform
import art
import random

clear = lambda: (
    os.system("cls") if platform.system() == "Windows" else os.system("clear")
)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)

playing = "y"
player_cards = []
dealer_cards = []

player_cards.append(random.choice(cards))
player_cards.append(random.choice(cards))
print(f"Your cards: {player_cards} Current Score: {sum(player_cards)}")

dealer_cards.append(random.choice(cards))
print(f"Computer's first card: {dealer_cards[0]}")

hit = input("Type 'y' to get another card, 'n' to pass.\n")

if hit == "n":
    print(f"Your final hand: {player_cards} Current Score: {sum(player_cards)}")

    while sum(dealer_cards) < sum(player_cards) or sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))

    print(f"Dealer's final Hand: {dealer_cards} Score: {sum(dealer_cards)}")

if sum(player_cards) > 21:
    print("You went over, you lose")
elif sum(dealer_cards) > 21:
    print("Dealer went over, you win")
elif sum(player_cards) == sum(dealer_cards):
    print("It's a draw")
elif sum(player_cards) > sum(dealer_cards):
    print("You win")
else:
    print("You lose")

# lost = False

# while playing == "y":
#     player_cards.clear()
#     player_cards.append(random.choice(cards))
#     player_cards.append(random.choice(cards))
#     print(f"Your cards: {player_cards} Current Score: {sum(player_cards)}")

#     dealer_cards.clear()
#     dealer_cards.append(random.choice(cards))
#     print(f"Computer's first card: {dealer_cards[0]}")
#     hit = input("Type 'y' to get another card, 'n' to pass.\n")

#     while hit == "y":
#         player_cards.append(random.choice(cards))
#         print(f"Your cards: {player_cards} Current Score: {sum(player_cards)}")
#         print(f"Computer's first card: {dealer_cards[0]}")

#         hit = "n"

#         if sum(player_cards) > 21:
#             lost = True
#         else:
#             hit = input("Type 'y' to get another card, 'n' to pass.\n")

#     while sum(dealer_cards) < 17 and lost == False:
#         dealer_cards.append(random.choice(cards))

#     print(
#         f"Your final hand: {player_cards} Current Score: {sum(player_cards)}"
#     )
#     print(f"Dealer's final Hand: {dealer_cards} Score: {sum(dealer_cards)}")

#     print("")

#     if lost == True:
#         print("You went over, you lose.")
#     elif sum(dealer_cards) > 21:
#         print("Dealer went over, you win.")
#     elif sum(dealer_cards) > sum(player_cards):
#         print("Dealer score is higher, you lose.")
#     elif sum(dealer_cards) < sum(player_cards):
#         print("Your score is higher, you win.")
#     else:
#         print("Draw")

#     playing = input("Do you want to play a game of Blackjack? 'y' or 'n'\n")
