word = input("Enter the word: ")
character = input("Enter the character: ")

count = 0
i = 0

while i < len(word):
    if word[i] == character:
        count += 1
    i += 1

print("Total occurances: ", count)