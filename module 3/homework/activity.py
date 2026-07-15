userinput = input("Enter your age: ")

try:
    age = int(userinput)
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
except ValueError:
    print("Invalid input. Please enter a valid age.")