# project.py

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    else:
        return num1 / num2

def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator in ('+', '-', '*', '/'):
                operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
                result = operations[operator](num1, num2)
                print(f"Result: {result}")
            else:
                print("Error: Invalid operator")

        except ValueError:
            print("Error: Invalid input. Please enter valid numeric values.")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()
