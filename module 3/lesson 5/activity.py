import random
playing = True
number = str(random.randint(0,9))

print("I will generate a number between 0 to 9, and you have to guess the number, one digit at a time.")

while playing:
    guess = input("Enter your guess: ")
    if number == guess:
        print("Congratulations! The number was ", number)
        break
    else:
        print("Wrong guess, try again!")