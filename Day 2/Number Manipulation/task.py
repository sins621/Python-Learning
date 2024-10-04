print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = total*(int(
    input("How much tip would you like to give? 10, 12, or 15? "))
             /100)
people = int(input("How many people to split the bill? "))
print(f"Each person should pay: $ {round((total+tip)/people,2)}")

