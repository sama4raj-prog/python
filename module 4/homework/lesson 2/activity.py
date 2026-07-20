hypotenuse = float(input("Enter the length of the hypotenuse: "))
opposite_side = float(input("Enter the length of the opposite side: "))
adjacent_side = float(input("Enter the length of the adjacent side: "))

# Calculate the sine, cosine, and tangent of the angle

sine = opposite_side / hypotenuse
cosine = adjacent_side / hypotenuse
tangent = opposite_side / adjacent_side

print("Sine:", sine)
print("Cosine:", cosine)
print("Tangent:", tangent)
