import os
import platform

import art

clear = lambda: (
    os.system("cls") if platform.system() == "Windows" else os.system("clear")
)

clear()
print(art.logo)

other_bidders = "yes"
bids = {}
highest_bid = 0
highest_bidder = ""

while other_bidders == "yes":
    # TODO-1: Ask the user for input
    name = input("What is your name?: \n")
    bid = int(input("What is your bid?: \n$"))
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = bid
    # TODO-3: Whether if new bids need to be added
    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'. \n"
    ).lower()
    clear()

# TODO-4: Compare bids in dictionary
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

