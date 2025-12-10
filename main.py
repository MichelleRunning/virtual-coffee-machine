MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
on = True


def report():
    """Print the current resources and money."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def make_drink(choice):
    """Subtract ingredients and make the drink."""
    for item in choice["ingredients"]:
        resources[item] -= choice["ingredients"][item]
    print("Here is your drink. Enjoy!\n")


def enough_resources(choice):
    """Checks if enough resources exist."""
    for item in choice["ingredients"]:
        if resources[item] < choice["ingredients"][item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def take_payment():
    """Ask user for coins and return total."""
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies


def process_payment(choice):
    """Handle payment logic."""
    global money
    payment = take_payment()

    if payment < choice["cost"]:
        print("Sorry, that's not enough money. Money refunded.\n")
        return False
    else:
        change = round(payment - choice["cost"], 2)
        money += choice["cost"]
        if change > 0:
            print(f"Here is your change: ${change}")
        return True


while on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        on = False

    elif user_choice == "report":
        report()

    elif user_choice in MENU:
        drink = MENU[user_choice]

        # 1. Check resources
        if enough_resources(drink):

            # 2. Process payment
            if process_payment(drink):

                # 3. Make drink
                make_drink(drink)

    else:
        print("Invalid selection.\n")
