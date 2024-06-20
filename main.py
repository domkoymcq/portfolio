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
    "water": 500,
    "milk": 500,
    "coffee": 200,
}
profit = 0


def sufficient(drink_ingredients):
    """determines if machine has enough resources for the selected drink"""
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """calculates total money paid from coins inserted"""
    print("Please insert coins")
    balance = int(input("How many quarters?: ")) *0.25
    balance += int(input("How many dimes?: ")) *0.1
    balance += int(input("How many nickles?: ")) *0.05
    balance += int(input("How many pennies?: ")) *0.01
    return balance

def funds(money_in,price):
    """return true when payment is accepted, otherwise false"""
    if money_in >= price:
        change = round(money_in - price, 2)
        print(f"Here is your ${change} in change")
        global profit
        profit += price
        return True
    else:
        print("Sorry that is not enough money")
        return False

def make_coffee(drink_name, order_ingredients):
    """deducts required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}:☕")

is_on = True
while True:
    choice = input("What would you like? espresso/latte/cappuccino: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[choice] # Selects an entry from the MENU dictionary, which is itself another dictionary
        if sufficient(drink["ingredients"]):
            payment = process_coins()
            if funds(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])









# TODO print report
# TODO 2 check resources are sufficient
# TODO 3 process coins
# TODO 4 check transaction is successful, else refund
# TODO 5 make coffee and update resources
