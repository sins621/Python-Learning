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

import art
import random


def sum_cards(hand):
    total = 0
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    for i in hand:
        if i == 11:
            if sum(hand) > 21:
                total += 1
            else:
                total += 11
        else:
            total += i
    return total


CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
hit = "y"

print(art.logo)
for i in range(2):
    player_cards.append(random.choice(CARDS))
    dealer_cards.append(random.choice(CARDS))

player_total = sum_cards(player_cards)
dealer_total = sum_cards(dealer_cards)

while hit == "y" and player_total < 22:
    print(f"Your cards: {player_cards} Current Score: {player_total}")
    print(f"Computer's first card: {dealer_cards[0]}")
    hit = input("Type 'y' to get another card, 'n' to pass.\n")
    if hit == "y":
        player_cards.append(random.choice(CARDS))
        player_total = sum_cards(player_cards)

print(f"Your final hand: {player_cards} Current Score: {player_total}")
while sum_cards(dealer_cards) < player_total or dealer_total < 17:
    dealer_cards.append(random.choice(CARDS))
    dealer_total = sum_cards(dealer_cards)
print(f"Dealer's final Hand: {dealer_cards} Score: {dealer_total}")

if player_total > 21:
    print("You went over, you lose")
elif dealer_total > 21:
    print("Dealer went over, you win")
elif player_total == dealer_total:
    print("It's a draw")
elif player_total > dealer_total:
    print("You win")
else:
    print("You lose")
