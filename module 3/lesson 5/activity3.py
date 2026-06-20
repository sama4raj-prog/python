import math

num = float(input("Enter a decimal number: "))
print(f"Floor value of {num}: ", math.floor(num))
print(f"Ceiling value of {num}: ", math.ceil(num))

x = 10
y = -15
print(math.copysign(x,y))

print("Factorial of 5: ", math.factorial(5))

print("GCD of 24, and 56: ", math.gcd(24,56))