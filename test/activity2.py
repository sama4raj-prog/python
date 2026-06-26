try: 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Select an operation(+, -, *, /): ")

    def add(num1, num2):
        return num1 + num2
    def subtract(num1, num2):
        return num1 - num2
    def multiply(num1, num2):
        return num1 * num2
    def divide(num1, num2):
        return num1 / num2
    
    if operation == '+':
        print("The sum of", num1, "and", num2, "is:", add(num1, num2))
    elif operation == '-':
        print("The difference of", num1, "and", num2, "is:", subtract(num1, num2))
    elif operation == '*':
        print("The product of", num1, "and", num2, "is:", multiply(num1, num2))
    elif operation == '/':
        print("The quotient of", num1, "and", num2, "is:", divide(num1, num2))

except ValueError:
    print("Invalid input. Please enter numeric values.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

