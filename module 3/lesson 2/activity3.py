def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fact(num-1)
    
print("The factorial of 0 is: ", fact(0))
print("The factorial of 1 is: ", fact(1))
print("The factorial of 3 is: ", fact(3))
print("The factorial of 5 is: ", fact(5))