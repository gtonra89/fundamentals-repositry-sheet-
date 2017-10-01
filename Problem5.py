# 5 - Guessing game
from random import randint

print("Guess a number between 1 and 50.")
secretNum = randint(0,50)
# Generate random int adapted from https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9

# Take input from the user and convert to int
userGuess = int(input("Your guess: "))

alreadyGuessed = []

# While guess is wrong, take more inputs
while userGuess != secretNum:
    if userGuess < secretNum: # If guess is too low, tell the user & ask for another input
        print("Too low, try again.")
        userGuess = int(input())
        alreadyGuessed.append(userGuess) # Add the guess to an array

    elif userGuess > secretNum: # If guess is too high, tell user & ask again
        print("Too high, try again.")
        userGuess = int(input())
        alreadyGuessed.append(userGuess) # Add guess to array

# If guess is right, tell user
if userGuess == secretNum:
    print("You're right!")
    print("It took you " + str(len(set(alreadyGuessed)) + 1) + " tries.") # +1 to count the last/correct guess.
    # Get number of individual elements in an array using length of unique set adapted from https://stackoverflow.com/questions/12282232/how-do-i-count-unique-values-inside-an-array-in-python
