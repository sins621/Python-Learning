from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
choice = ""
CoffeeMaker = CoffeeMaker()
Menu = Menu()
MoneyMachine = MoneyMachine()

while is_on == True:
    choice = input(f"What would you like? ({Menu.get_items()})\n")
    if choice == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    elif choice == "off":
        is_on = False
    else:
        order = Menu.find_drink(choice)
        if CoffeeMaker.is_resource_sufficient(order):
            if MoneyMachine.make_payment(order.cost):
                CoffeeMaker.make_coffee(order)
