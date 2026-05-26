import random

num = random.randint(1,50)

hearts = 5

print("Welcome to the Number Guessing Game! You have five hearts. Too cold means the input is greater than the number. Too hot means the input is less than the number. Good luck!")

if hearts > 0 or guess != num:
    guess = print(input("Guess the number between 1 and 50: "))

if guess > num: 
    print("Too cold. Try again.")
    hearts = hearts-1
    print("You have ", hearts, " hearts left.")
elif guess < num:  
    print("Too hot. Try again.")
    hearts = hearts-1
    print("You have ", hearts, " hearts left.")

if guess == num:
    print("Congratulations, You guessed the number!")

if hearts == 0:
    print("You lose. The number was ", num)

