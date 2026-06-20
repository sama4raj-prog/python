import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"You chose {user_action}, and computer chose {computer_action}.")

    if user_action == computer_action:
        print("IT'S A TIE!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("ROCK SMASHES SCISSORS! YOU WIN!")
        else:
            print("PAPER COVERS ROCK! YOU LOSE.")
        
    elif user_action == "scissors":
        if computer_action == "paper":
            print("SCISSORS CUT PAPER! YOU WIN.")
        else:
            print("ROCK SMASHES SCISSORS! YOU LOSE!")

    elif user_action == "paper":
        if computer_action == "rock":
            print("PAPER COVERS ROCK! YOU WIN.")
        else:
            print("SCISSORS CUT PAPER! YOU LOSE!")
            
    playAgain = input("Play again? (y/n): ").lower()
    if playAgain == "n":
        break