from menu import MENU

VALID_INPUTS = {"report", "off", "espresso", "latte", "cappuccino"}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report():
    print()

    for key, value in resources.items():
        if key == "money":
            print(f"{key.capitalize()}: ${value:.2f}")
        else:
            print(f"{key.capitalize()}: {value}ml")

    print()


def insert_coins():
    coins = {"quarters": 0.25, "dimes": 0.50, "nickles": 0.10, "pennies": 0.01}
    total_cash = 0

    print("Please, insert coins.")

    for coin, value in coins.items():
        current_coin_name = coin
        coin = input(f"How many {current_coin_name}? ")

        while not coin.isdigit() or int(coin) < 0:
            print("Invalid input...")
            coin = input(f"How many {current_coin_name}? ")

        total_cash += int(coin) * value

    return total_cash


def make_coffee(coffee_name):
    global resources
    current_machine_state = resources.copy()

    price = MENU[coffee_name]["cost"]
    required_ingredients = MENU[coffee_name]["ingredients"].items()
    available_resources = resources.items()

    for ingredient_key, ingredient_value in required_ingredients:
        for resource_key, resource_value in available_resources:
            if resource_key == ingredient_key:
                if ingredient_value > resource_value:
                    print(f"Not enough {resource_key}")
                    return
                else:
                    resources[resource_key] -= ingredient_value
    money = insert_coins()

    if money < price:
        print("Sorry that's not enough. Money refunded")

        resources = current_machine_state
        print(resources)
        return

    if money > price:
        print(f"Here is ${money - price:.2f} in change.")

    resources["money"] += price
    print(f"Here is your {coffee_name} ☕.")


def get_user_input():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    while user_input.lower() not in VALID_INPUTS:
        print("Invalid input...")
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

    return user_input.lower()


def handle_input(input_value):
    if input_value == "off":
        return False

    if input_value == "report":
        report()

    else:
        make_coffee(input_value)
