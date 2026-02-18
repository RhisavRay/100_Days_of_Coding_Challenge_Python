import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

print(art.logo)

first_num = int(input("Enter first number: "))

decision = "y"

while decision == "y":
    print("+\n-\n*\n/\n**\n")
    operation = input("Pick an operation: ")
    second_num = int(input("Enter second number: "))

    if operation == "+":
        result = add(first_num, second_num)
    elif operation == "-":
        result = subtract(first_num, second_num)
    elif operation == "*":
        result = multiply(first_num, second_num)
    elif operation == "/":
        result = divide(first_num, second_num)
    elif operation == "**":
        result = exponent(first_num, second_num)
    else:
        print("Invalid operation")

    print(f"{first_num} {operation} {second_num} = {result}")

    decision = input("Do you want to continue? (y/n): ")
    first_num = result