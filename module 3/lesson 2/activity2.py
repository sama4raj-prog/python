def cube(number):
    return number**3

def divisibleBy3(number):
    if number%3 == 0:
        return cube(number)
    else:
        return False
    
number = int(input("Enter a number: "))
print(divisibleBy3(number))