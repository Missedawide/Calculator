def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

print("Select Calculation (Case Sensitive!):")

choice = input(" ( Add, Subtract, Multiply, Divide ) ")

try:
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))

    if choice == 'Add':
        print("Answer:", addition(num1, num2))
    elif choice == 'Subtract':
        print("Answer:", subtraction(num1, num2))
    elif choice == 'Multiply':
        print("Answer:", multiplication(num1, num2))
    elif choice == 'Divide':
        print("Answer:", division(num1, num2))
    else:
        print("Invalid input")
except ValueError:
    print("Invalid Number.")