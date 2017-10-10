
import random

guessesLeft = 5
guesses = 0

numberToGuess = random.randint(1, 101)

while guessesLeft > 0:
    userGuess = int(input("Please enter a number between 1 and 100: "))
    guesses += 1
    guessesLeft -= 1
    if userGuess == numberToGuess:
        print(f"Hooray! You guessed the number in {guesses} guesses!")
        answer = input("Do you want to play again? (Type Y or N) ")
        if answer == "Y" or answer == "y":
            guesses = 0
            guessesLeft = 5
        elif answer == "N" or answer == "n":
            print("Thanks for playing!")
            guessesLeft = 0
    elif userGuess > numberToGuess and guessesLeft > 0:
        print("Too high. Try guessing a little lower this time")
    elif userGuess < numberToGuess and guessesLeft > 0:
        print("Too low. Aim higher this time")
    elif userGuess != numberToGuess and guessesLeft == 0:
        print(f"Too bad, you ran out of turns, the number was {numberToGuess}. Better luck next time.")
