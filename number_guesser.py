
import random

def main():
    guesses_left = 5
    guesses = 0

    number_to_guess = random.randint(1, 100)

    while guesses_left > 0:
        user_guess = int(input("Please enter a number between 1 and 100: "))
        guesses += 1
        guesses_left -= 1

        if user_guess == number_to_guess:
            print(f"Hooray! You guessed the number in {guesses} guesses!")
            ask_to_play_again()
        elif user_guess > number_to_guess and guesses_left > 0:
            print("Too high. Try guessing a little lower this time")
        elif user_guess < number_to_guess and guesses_left > 0:
            print("Too low. Aim higher this time")
        elif user_guess != number_to_guess and guesses_left == 0:
            print(f"Too bad, you ran out of turns, the number was {number_to_guess}. Better luck next time.")
            ask_to_play_again()

def ask_to_play_again():
    answer = input("Do you want to play again? (Type Y or N) ")
    if answer == "Y" or answer == "y":
        main()
    elif answer == "N" or answer == "n":
        print("Thanks for playing!")
        guesses_left = 0

if __name__ == '__main__':
    main()
