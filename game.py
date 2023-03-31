import os
import random
from Dev import *

while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        print(f"YOUR CHIP : {cP()} || COMPUTER CHIP : {cC()} ")
        print("==========================================")
        bet1 = int(input("YOUR BET : "))
        bet2 = int(input("COMPUTER BET : "))
        player = input("rock, paper, or scissors : ").lower()
        os.system('cls')

    if player == computer:
        print(f"computer: {computer}")
        print(f"player: {player}")
        print("TIE")
    elif player == "rock":
        if computer == "paper":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("LOSE")
            lose(bet1,bet2)
        if computer == "scissors":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("WIN")
            win(bet1,bet2)
    elif player == "scissors":
        if computer == "paper":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("WIN")
            win(bet1,bet2)
        if computer == "rock":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("LOSE")
            lose(bet1,bet2)
    elif player == "paper":
        if computer == "scissors":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("LOSE")
            lose(bet1,bet2)
        if computer == "rock":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("WIN")
            win(bet1,bet2)
    
    play_again = input("Play Again? (yes/no): ").lower()
    os.system('cls')
    if cP() <= 0 or cC() <= 0:
        print(f"Not Enough Chip!\n")
        break

    if play_again != "yes":
        break


print(f"YOUR CHIP      : {cP()}")
print(f"COMPUTER CHIP  : {cC()}")

# Inspired by anime (Kakegurui / Compulsive Gambler)

