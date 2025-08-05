def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def calculator():
    print("Welcome to the Command-Line Calculator!")
    print("Type 'exit' at any time to quit.\n")

    while True:
        try:
            num1 = input("Enter the first number: ")
            if num1.lower() == 'exit':
                break
            num1 = float(num1)

            operator = input("Choose an operation (+, -, *, /): ")
            if operator.lower() == 'exit':
                break
            if operator not in ['+', '-', '*', '/']:
                print("Invalid operator. Please choose from +, -, *, /.")
                continue

            num2 = input("Enter the second number: ")
            if num2.lower() == 'exit':
                break
            num2 = float(num2)

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)

            print(f"Result: {num1} {operator} {num2} = {result:.2f}\n")

        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")

    print("Thanks for using the calculator. Goodbye!")

# Run the calculator
calculator()