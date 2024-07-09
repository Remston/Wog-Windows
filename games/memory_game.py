import time
from score.score import update_score
from utils import cls, compare_results, print_result, continue_play, restart_main, generate_number, get_guess_from_user


def play_memory_game(difficulty):
    cls()
    print("Welcome to Memory Game!")
    limit = 101
    random_list = generate_sequence(difficulty, limit)
    print("Memorize the list of numbers:")
    time.sleep(3.5)
    print(random_list)
    time.sleep(0.7)
    cls()
    user_list = get_list_from_user(difficulty, limit)
    win = compare_results(user_list, random_list)
    if win:
        update_score(difficulty)
    print_result(win, random_list)
    again = continue_play()
    if again:
        restart_main()
    else:
        return


def generate_sequence(difficulty, limit):
    random_list = []
    while len(random_list) < difficulty:
        random_number = generate_number(1, limit)
        if random_number not in random_list:
            random_list.append(random_number)
    return random_list


def get_list_from_user(difficulty, limit):
    user_list = []
    for i in range(difficulty):
        guess = get_guess_from_user(i, limit, difficulty)
        user_list.append(guess)
    return user_list
