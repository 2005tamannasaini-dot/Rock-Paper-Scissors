## Rock Paper Scissors Game

import random

print("=== Welcome to Rock Paper Scissors Game. ===")

choose = ["rock", "paper", "scissors"]
computer_choice = random.choice(choose)

computer_score = 0
user_score = 0

user_choice = input("please choose(Rock/Paper/Scissors) :").lower()

if user_choice not in choose:
    print("Invalid choice! Please choose rock, paper, or scissors.")
    
else:
    print("your choice:", user_choice)
    print("Computer choice:", computer_choice )

    if computer_choice == user_choice:
        print("It's a draw.")

    elif ((computer_choice == "rock" and user_choice == "paper")
        or (computer_choice == "paper" and user_choice == "scissors") 
        or (computer_choice == "scissors" and  user_choice == "rock")):
        print("you win!.")
        user_score += 1

    else:
        print("computer wins!.") 
        computer_score += 1 

    print("your score:", user_score)
    print("computer score:", computer_score)      
      

