print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height < 120:
    print("Sorry you have to grow taller before you can ride.")
else:
    age = int(input("How old are you?\n"))
    price = 0
    if age > 18:
        price = 12
    elif age > 11:
        price = 7
    else:
        price = 5
    print(f"You can ride the rollercoaster, it will be ${price}.")
