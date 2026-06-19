"""
Work flow of Project -

1- Input from user (Rock,Paper,Scissors)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result priint


Cases : A - ROCK

Rock - Rock = Tie
Rock - Paper = Paper win
Rock - Scissors = Rock win

Cases : B - Paper

Paper - Paper = Tie
Paper - Rock = Paper win
Paper - Scissors = Scissors win

Cases : C - Scissors

Scissors - Scissors = Tie
Scissors - Rock = Rock win
Scissors - Paper = Scissors win

"""

import random

item_list = ["Rock", "Paper", "Scissors"]

user_choice = input("Enter your move = Rock, Paper, Scissors = ")
comp_choice = random.choice(item_list)

print(f"user_choice = {user_choice}, computer choice = {comp_choice}")


if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")
