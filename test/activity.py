import random

num = random.randint(1,50)

hearts = 5

print("Welcome to the Number Guessing Game! You have five hearts. Too cold means the input is greater than the number. Too hot means the input is less than the number. Good luck!")

while hearts > 0:
    print(f"Hearts left: {hearts}")
    try:
        guess = int(input("Enter a number between 1-50: "))
    except ValueError:
        print("Please enter a valid integer.")
        exit()
    if guess == num:
        print(f"Congratulations! You guessed the secret number {num}!")
        break
    else:
        hearts -= 1
    if guess > num: 
        print("Try again. Hint: Too cold.")
        print("You have ", hearts, " hearts left.")
    elif guess < num:  
         print("Try again. Hint: Too hot.")
         print("You have ", hearts, " hearts left.")

if hearts == 0:
    print(f"Game over! The secret number was {num}. Better luck next time!")


