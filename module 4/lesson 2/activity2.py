my_tuple = (1,2,3,3,2,1)
my_tuple1 = (1,2,3,4,5,6)

if my_tuple == my_tuple[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

if my_tuple1 == my_tuple[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")