## Rock Paper Scissors Game

import random

print("=== Welcome to Rock Paper Scissors Game. ===")

choose = ["rock", "paper", "scissors"]
computer_choice = random.choice(choose)


user_choice = input("please choose(Rock/Paper/Scissors) :").lower()

print("your choice:", user_choice)
print("Computer choice:", computer_choice )

if computer_choice == user_choice:
    print("It's a draw.")

elif ((computer_choice == "rock" and user_choice == "paper")
       or (computer_choice == "paper" and user_choice == "scissors") 
      or (computer_choice == "scissors" and  user_choice == "rock")):
    print("you win!.")

else:
    print("computer wins!.")    

