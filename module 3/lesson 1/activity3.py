def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

choice = input("Please select an operation(a,b,c,d): \na) add\nb) subtract\nc) multiply\nd) divide.")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if choice == 'a':
    print(f"{a}+{b}= {add(a,b)}")
elif choice == 'b':
    print(f"{a}-{b}= {subtract(a,b)}")
elif choice == 'c':
    print(f"{a}*{b}= {multiply(a,b)}")
elif choice == 'd':
    print(f"{a}/{b}= {divide(a,b)}")
else:
    print("Invalid input")