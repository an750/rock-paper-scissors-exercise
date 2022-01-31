def RPS():

# this is the "game.py" file...
    print("Rock, Paper, Scissors, Shoot!")

# ASK FOR USER INPUT
    print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
    user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ").lower()
    print("User Chose:", user_choice)  # figure out how to gracefully leave


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
