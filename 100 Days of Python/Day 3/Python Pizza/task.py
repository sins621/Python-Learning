print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total = 0

SMALL_PIZZA_PRICE = 15
MEDIUM_PIZZA_PRICE = 20
LARGE_PIZZA_PRICE = 25
SMALL_PEPPERONI_PRICE = 2
MEDIUM_LARGE_PEPPERONI_PRICE = 2
CHEESE_PRICE = 1

if extra_cheese == "Y":
    total += CHEESE_PRICE
if pepperoni == "Y":
    if size == "S":
        total += SMALL_PEPPERONI_PRICE;
    else:
        total += MEDIUM_LARGE_PEPPERONI_PRICE;
if size == "S":
    total += SMALL_PIZZA_PRICE;
elif size == "M":
    total += MEDIUM_PIZZA_PRICE;
else:
    total += LARGE_PIZZA_PRICE;

print(f"Your total is: ${total}.")
