## Rock Paper Scissors Game

import random

print("=== Welcome to Rock Paper Scissors Game. ===")

choose = ["rock", "paper", "scissors"]
computer_choice = random.choice(choose)

user_input = input("please choose(Rock/Paper/Scissors) :").lower()

print("your choice:", user_input)
print("Computer choice:", computer_choice )

