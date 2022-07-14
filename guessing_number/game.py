import random

"""
It's a Guessing a Number game:
1 - You guess a number
2 - The computer guides you to approach the answer
3 - The computer counts the number of your trials
4 - The computer asks the user, you, to play again
"""

intention = 'Y'  # initiate the game

while intention == 'Y':  # create a while-loop if the intention of the player to play is True
    answer = random.randint(1, 100)  # pseudorandom number is created by the python lib called random
    counter = 0

    """Every attempt of the player is counted so once the game is finished a messagem will congratulate the user"""
    try:
        play = int(input("Guess a number between 1 and 100: "))  # Bid of the player is transformed from type string to integer
    except ValueError:  # if the contender input a type that wasn't capable of being converted into an integer, then
        # the massage "Sorry. This ain't a integer" will appear.
        print("Sorry. This ain't an integer")
    else:
        counter += 1  # if the input 'play' is compatible with the code, then the counter will increase a try
        while play != answer:  # Every time that the bid is in contrast to the answer the counter will increase a unit
            if play > answer:
                print("Your number is too large.")
                counter += 1
            else:
                print("Your number is too small.")
                counter += 1

            try:  # the question will repeat until the player guess right and the tips "Your number is too large."
                # and "Your number is too small." will guide it.
                play = int(input("Guess a number between 1 and 100: "))
            except ValueError:
                print("Sorry. This ain't a integer")
                break

        if play == answer:
            counter += 1
            print("You got it! You tried " + str(counter) + " times.")
            intention = input("Continue?[Y/N] ").upper()

        while intention not in ["N", "Y"]:  # validation.
            intention = input("Please type again. Continue?[Y/N] ").upper()  # while the answer to the question "Continue?[Y/N] "
            # didn't is "Y" or "N" the program will ask again.
        if intention == "N":  # if the intention to play again is "N" for no then the code will finish
            break
        elif intention == "Y":  # if it's "Y" then the code will return to the beginning and generate another pseudorandom number
            intention = "Y"






