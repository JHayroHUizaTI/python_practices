from random import randint
from art import logo

EASY_LEVEL_TURNS = 14
HARD_LEVEL_TURNS = 7


def check_answer(guess, answer, turns):
    """Check answer against guess. Return the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"you got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"psst, the correct answer is {answer}")

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you're run out of guesses, you lose...")
            return
        elif guess != answer:
            print("Guess again...")


game()
