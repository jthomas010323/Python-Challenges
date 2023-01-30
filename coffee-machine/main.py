MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${resources['money']}")


def calculate_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total


def make_coffee(coffee):
    if resources['water'] >= MENU[coffee]['ingredients']['water'] and resources['milk'] >= MENU[coffee]['ingredients']['milk'] and resources['coffee'] >= MENU[coffee]['ingredients']['coffee']:
        total = float(calculate_coins())
        change = total - MENU[coffee]["cost"]
        if change <= 0:
            print("Sorry, not enough money. Money refunded")
        else:
            print(f"Here's ${change:.2f} in change.")
            print(f"Here's your {coffee}. Enjoy")
            resources['water'] -= MENU[coffee]['ingredients']['water']
            resources['milk'] -= MENU[coffee]['ingredients']['milk']
            resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
            resources['money'] += MENU[coffee]['cost']
    else:
        if resources['water'] < MENU[coffee]['ingredients']['water']:
            refill_choice=input("Sorry, Not enough water. Want to refill?: ").lower()
            if refill_choice == "yes":
                refill()
            else:
                print("No refill")
        elif resources["milk"] < MENU[coffee]['ingredients']['milk']:
            refill_choice = input("Sorry, Not enough milk. Want to refill?: ").lower()
            if refill_choice == "yes":
                refill()
            else:
                print("No refill")
        elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
            refill_choice = input("Sorry, Not enough coffee. Want to refill?: ").lower()
            if refill_choice == "yes":
                refill()
            else:
                print("No refill")


def refill():
    print("in refill")
    fill_water = int(input("How much water?: "))
    fill_milk = int(input("How much milk?: "))
    fill_coffee = int(input("How much coffee?: "))
    resources["water"] += fill_water
    resources["milk"] += fill_milk
    resources["coffee"] += fill_coffee


water = True
coffee = True
while water and coffee:
    order = input("What would you like to order? (espresso/latte/cappuccino): ").lower()
    if order == "exit" or order == "quit" or order == "no":
        break
    elif order == "report":
        print_report()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        make_coffee(order)
    else:
        print("That's not an option")
    if resources["water"] < 50:
        refill_choice = input("Low on resources, want to refill?: ").lower()
        if refill_choice == "yes":
            refill()
        else:
            water = False
    if resources["coffee"] < 18:
        refill_choice = input("Low on resources, want to refill?: ").lower()
        if refill_choice == "yes":
            refill()
        else:
            coffee = False
print("Enjoy your day")