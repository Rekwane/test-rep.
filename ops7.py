# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?

import random
game_number = random.randint(1, 20)
user_number = int(input("Welcome to the number guessing game! enter a number between 1 and 20: "))
attempts = 0

while game_number > user_number:
    print("Your number is too  low!")
    user_number = (int(input("enter a number: ")))

while user_number > game_number:
    print("Your number is too high")
    user_number = (int(input("enter a number: ")))

while user_number == game_number:
    print(F'("yes! you guessed it in {attempts} tries")')
    break

