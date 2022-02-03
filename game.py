# this is the "game.py" file...
import os

# DETERMINE THE WINNER / FINAL RESULTS

def determine_winner(user_choice, computer_choice):
    hold_winner = ""
    if user_choice == "rock" and computer_choice == "paper":
        print("Computer Chose:", computer_choice)
        print("You lose!")
        hold_winner='paper'
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Computer Chose:", computer_choice)
        print("You lose!")
        hold_winner = 'scissors'
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Computer Chose:", computer_choice)
        print("You lose!")
        hold_winner = 'rock'
    elif user_choice == "paper" and computer_choice == "rock":
        print("Computer Chose:", computer_choice)
        print("You Win!")
        hold_winner = 'paper'
    elif user_choice == "rock" and computer_choice == "scissors":
        print("Computer Chose:", computer_choice)
        print("You Win!")
        hold_winner = 'rock'
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Computer Chose:", computer_choice)
        print("You Win!")
        hold_winner = 'scissors'
    elif user_choice == computer_choice:
        print("Computer Chose:", computer_choice)
        print("It's a tie!")
        hold_winner = None

    return hold_winner

if __name__ == "__main__":
    player_name = os.getenv("PLAYER_NAME", default="Player One")

# ASK FOR USER INPUT
    print("Welcome", player_name, "to my Rock-Paper-Scissors game...")
    user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ").lower()
    print("User Chose:", user_choice)

# VALIDATIONS
    answers = ["rock", "paper", "scissors"]
    if user_choice not in answers:
        print("Sorry, your input was not valid. Please try again!")
        quit()

# COMPUTER CHOICE
    import random
    computer_choice = random.choice(["rock","paper","scissors"])
# CALL FUNCTION
    determine_winner(user_choice, computer_choice)

    print("Thanks for playing. Please play again!")
