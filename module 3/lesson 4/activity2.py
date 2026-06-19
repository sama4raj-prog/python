try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Division by zero is an error.")
except SyntaxError:
    print("Coma is missing.")
except: 
    print("wrong input !")
else:
    print("no exceptions.")
finally:
    print("this will execute no matter what.")