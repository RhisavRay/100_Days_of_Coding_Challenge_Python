import helper_data


def report():
    for key in helper_data.resources:
        if key == "coffee":
            print(f"{key}: {helper_data.resources[key]}g")
        else:
            print(f"{key}: {helper_data.resources[key]}ml")


def take_order():
    print("Here are our menu items")
    for key in helper_data.menu:
        print(f"{key}: ${helper_data.menu[key]["cost"]}")

    order = input("\nWhich one would you like to order? Enter the name of the drink: ").lower()

    return order


def check_possibility(order):
    possible, ingredient = True, None
    for key in helper_data.menu[order]["ingredients"]:
        if helper_data.menu[order]["ingredients"][key] > helper_data.resources[key]:
            possible = False
            ingredient = key
            break
    return possible, ingredient


def place_order(order):
    amount = 0.0
    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickels": 0,
        "pennies": 0,
    }

    print("Please mention the number of each coin you are giving")
    for coin in coins:
        count = int(input(f"{coin}: "))
        coins[coin] = count
        if coin == "quarters":
            amount += count * 0.25
        elif coin == "dimes":
            amount += count * 0.1
        elif coin == "nickels":
            amount += count * 0.05
        else:
            amount += count * 0.01

        if amount >= helper_data.menu[order]["cost"]:
            break

    if amount < helper_data.menu[order]["cost"]:
        print("Sorry. You don't have enough money. The money has been refunded.")
    else:
        if amount > helper_data.menu[order]["cost"]:
            print(f"Here is your change of ${amount - helper_data.menu[order]['cost']:.2f}$")
        print(f"Here is your {order}. Enjoy!")

        for ingredient in helper_data.menu[order]["ingredients"]:
            helper_data.resources[ingredient] -= helper_data.menu[order]["ingredients"][ingredient]