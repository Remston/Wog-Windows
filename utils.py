import os
import random
from multipledispatch import dispatch

file_path = 'score\\scores.txt' if os.name == 'nt' else 'score/scores.txt'
error = 6982827982


def generate_number(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)


def validate_input(user_input, limit):
    if not (user_input.isdigit() and 0 < int(user_input) <= limit):
        print("Wrong input. Try again.")
        return True
    return False


def print_result(win, secret_number):
    if win:
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose!")
    print("Riddle was:\t" + str(secret_number))


def continue_play():
    check = True
    game = ''
    while check:
        game = input("Game ended. Do you want play again? (Y/N)\t")
        if not (game.isalpha() and (game.lower() == 'n' or game.lower() == 'y')):
            print("Wrong input. Try again.")
            check = True
        else:
            game = game.lower()
            check = False
    if game == 'y':
        print()
        return True
    else:
        return False


@dispatch(int, int)
def compare_results(user_guess, random_num):
    return user_guess == random_num


@dispatch(list, list)
def compare_results(user_guess, random_num):
    return user_guess == random_num


@dispatch(int, tuple)
def compare_results(guess, interval):
    return interval[0] <= guess <= interval[1]


def cls():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux or macOS
        os.system('clear')


def wright_file(file_path, score, error):
    try:
        with open(file_path, "w+") as file:
            file.write(str(score))
    except IOError:
        return error
    return 0


def read_file(file_path, error):
    try:
        with open(file_path, 'r') as file:
            score = file.read().strip()
            if score:
                return int(score)
            else:
                return error
            return int(score)
    except IOError:
        return error
    except ValueError:
        return error


def restart_main():
    os.system('python main.py')


@dispatch(int)
def get_guess_from_user(difficulty):
    guess = 0
    check = True
    while check:
        guess = input(f"Guess a number between 0 and {difficulty}: \t")
        if validate_input(guess, difficulty):
            continue
        else:
            check = False
    return int(guess)


@dispatch(int, int)
def get_guess_from_user(random_number, limit):
    guess = 0
    check = True
    while check:
        guess = input(f"You have {random_number} USD. Guess how much it's in ILS\t")
        if validate_input(guess, limit * 10):
            continue
        else:
            check = False
    return int(guess)


@dispatch(int, int, int)
def get_guess_from_user(i, limit, difficulty):
    guess = 0
    check = True
    while check:
        guess = input(f"Enter {i + 1} number:\t")
        if validate_input(guess, limit):
            continue
        else:
            check = False
    return int(guess)
