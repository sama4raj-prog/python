x = 5
y = "Alex"

print(x)
print(y)

#User Input
name = input("What is your name? ")
print("Hello, " + name + " !")

import keyword

#Check if a word is a Python keywords
word = input("Enter a word: ")
print(keyword.iskeyword(word))

#Printing all Python keywords
print(keyword.kwlist)