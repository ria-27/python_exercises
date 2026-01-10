#Program to build a basic calculator

def calculator():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Division: undefined")
calculator()