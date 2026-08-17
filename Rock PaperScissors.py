## Rock Paper Scissors Game

import random

print("=== Welcome to Rock Paper Scissors Game. ===")

choose = ["rock", "paper", "scissors"]

def get_result(user_choice, computer_choice):
    if computer_choice == user_choice:
        return "It's a draw."

    elif ((computer_choice == "rock" and user_choice == "paper")
        or (computer_choice == "paper" and user_choice == "scissors") 
        or (computer_choice == "scissors" and  user_choice == "rock")):
        return "you win!."

    else:
        return "computer wins!"
    
def get_user_choice():
    while True:
        
        user_choice = input("please choose(Rock/Paper/Scissors) :").lower()
        if user_choice in choose:
            return user_choice
        
        else:
            print("Invalid choice! Please choose rock, paper, or scissors.")

def play_game():
    computer_score = 0
    user_score = 0

    while True:
        computer_choice = random.choice(choose)    
        user_choice = get_user_choice()

        print("your choice:", user_choice)
        print("Computer choice:", computer_choice )

        result = get_result(user_choice, computer_choice)
        print(result)

        if result == "you win!.":
            user_score += 1

        elif result == "computer wins!":
            computer_score += 1

        if not play_again(): 
            show_final_result(user_score, computer_score)              
            return   

def show_final_result(user_score, computer_score):
    print("Game Over!")
    print("your score:", user_score)
    print("computer score:", computer_score) 
            
    if user_score > computer_score:
        print("you are the winner. 🎉") 
            
    elif computer_score > user_score:
        print("computer is the winner.")
            
    else:
        print("It's a Draw")         
            
def play_again():
    while True:
        choice = input("Play Again?(yes/no):").lower()
        if choice == "yes":
            return True

        elif choice == "no":
            return False

        else:
            print("please! choose only yes or no.")            
                
play_game()        