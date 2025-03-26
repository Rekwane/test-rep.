# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
# Do not just google the game and copy paste, If you would like to look at a completed version if you get stuck on a step please do so.
#Write your code below this line:

import random

selection = input("choose your weapon! rock/paper/scissors: ")
weapon = {selection}
game_weapon = ["rock", "paper", "scissors"]
game_weapon = random.choice(game_weapon)
if game_weapon == "rock" and selection == "paper":
    print("paper beats rock! you win!")
elif game_weapon == "paper" and selection == "scissors":
    print("scissors beat paper! you win!")
elif game_weapon == "scissors" and selection == "rock":
    print("rock beats scissors! you win!")
elif selection == "gun":
    print("it's just a game!")
elif game_weapon == selection:
    print("it is a tie")
elif selection != "rock" or "paper" or "scissors" or "gun":
    print("invalid entry")
else:
    print("sorry you lose!")
