import random

number = 0
guess = 0
result = None
lives = 5
trys = [0]

number = random.randint(0, 20)

while result == None:
    print("Lives: ", lives)
    guess = input("Enter a number between 0-20 and try guess the correct one:     ")
    for x in trys:
        if x == guess:
            print("You have used that number already!")
            lives+=1

    if number == guess:
        print("Correct!")
        result = True
    elif number > guess:
        print("Guess is too small!")
        lives-=1
    elif number < guess:
        print("Guess is too large!")
        lives-=1

    if lives == 0:
        result = False
    trys.append( guess )

if result == True:
    print("Well done you completed the guessing game")
elif result == False:
    print("Sorry better luck next time")