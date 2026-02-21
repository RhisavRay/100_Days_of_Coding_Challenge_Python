import helper_data, helper_functions


print("Welcome to the Coffee Machine App")

repeat = True
while repeat:
    function = input("What would you like to do? Report or Order: ").lower()

    if function == "report":
        helper_functions.report()
    elif function == "order":
        order = helper_functions.take_order()
        if order in helper_data.menu:
            possible, ingredient = helper_functions.check_possibility(order)
            if not possible:
                print(f"Sorry. Can't make this order now. Not enough {ingredient} in the machine")
            else:
                helper_functions.place_order(order)
        else:
            print("That is not a valid option")
    else:
        print("Invalid entry")

    repeat = True if input("Do you want to continue? Type 'yes' or 'no': ").lower() == "yes" else False

print("Thank you for visiting the Coffee Machine App")