def RPS():

# this is the "game.py" file...
    import os
    player_name = os.getenv("PLAYER_NAME", default="Player One")
    #NEED TO WRITE IN README

# ASK FOR USER INPUT
    print("Welcome" + player_name + "to my Rock-Paper-Scissors game...")
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

# DETERMINE THE WINNER / FINAL RESULTS
    if user_choice == "rock" and computer_choice == "paper":
        print("Computer Chose:", computer_choice)
        print ("You lose!")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Computer Chose:", computer_choice)
        print("You lose!")
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Computer Chose:", computer_choice)
        print("You lose!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("Computer Chose:", computer_choice)
        print("You Win!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("Computer Chose:", computer_choice)
        print("You Win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Computer Chose:", computer_choice)
        print("You Win!")
    elif user_choice == computer_choice:
        print("Computer Chose:", computer_choice)
        print("It's a tie!")

    print("Thanks for playing. Please play again!")

RPS()
