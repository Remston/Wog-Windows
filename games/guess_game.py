from score.score import update_score
from utils import cls, generate_number, get_guess_from_user, compare_results, print_result, continue_play, restart_main


def play_guess_game(difficulty):
    cls()
    print("Welcome to Guess Game!")
    secret_number = generate_number(0, difficulty)
    guess = get_guess_from_user(difficulty)
    win = compare_results(guess, secret_number)
    if win:
        update_score(difficulty)
    print_result(win, secret_number)
    again = continue_play()
    if again:
        restart_main()
    else:
        return
