from random import randint

easy_level_turns = 10
hard_level_turns = 5
turns = 0


def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The number was {answer}.")


def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # print(answer)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guess. You loose.")
            print(f"The number was {answer}")
            return
        elif guess != answer:
            print("Guess again.")


game()
