from data import MENU, resources, user_coins


def print_resources(resources):
    for resource, amount in resources.items():
        print(f"{resource.capitalize()} : {amount}")


def subtract_resources(resources, ingredients):
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount


def can_make_coffee(resources, ingredients):
    for ingredient, amount in ingredients.items():
        if resources.get(ingredient, 0) < amount:
            return f"Sorry, there is not enough {ingredient}."
    return True


def user_total(user_coins):
    total = 0
    for coin in user_coins:
        total += user_coins[coin]["value"] * user_coins[coin]["amount"]
    return total


machine_power = "on"
inserting_coins = "y"


while machine_power == "on":
    coffee_option = input(
        "What would you like? (espresso/latte/cappuccino)\n"
    ).lower()

    if coffee_option == "off":
        machine_power = "off"
    elif coffee_option == "report":
        print_resources(resources)
    elif coffee_option in MENU:
        option_ingredients = MENU[coffee_option]["ingredients"]
        check_resources = can_make_coffee(resources, option_ingredients)

        if check_resources is True:
            print(f"The espresso costs: ${MENU[coffee_option]["cost"]}")
            while inserting_coins == "y":
                coin_option = input(
                    "Please insert a coin. (quarter/dime/nickle/penny)\n"
                ).lower()

                coin_amount = int(
                    input(f"How many {coin_option} are you inserting?\n")
                )

                user_coins[coin_option]["amount"] += coin_amount

                print(f"Current amount inserted: ${user_total(user_coins)}")
                inserting_coins = input(
                    "Would you like to insert another coin? (y/n) \n"
                ).lower()

            total = user_total(user_coins)
            if total > MENU[coffee_option]["cost"]:
                resources["money"] += total
                subtract_resources(resources, option_ingredients)
                print(f"Here is your {coffee_option} ☕. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")
            pass
        else:
            print(check_resources)
    else:
        print("Invalid option. Please choose from the menu.")
