from score.score import update_score
from currency_converter import CurrencyConverter
from utils import continue_play, generate_number, compare_results, print_result, cls, restart_main,  \
    get_guess_from_user


def play_currency_roulette_game(difficulty):
    cls()
    limit = 100
    print("Welcome to Currency Roulette Game!")
    random_number = generate_number(1, limit)
    c = CurrencyConverter()
    value_after_exchange = c.convert(random_number, 'USD', 'ILS')
    if value_after_exchange is not None:
        interval = get_money_interval(difficulty, value_after_exchange)
        secret_number = int(value_after_exchange)
        guess = get_guess_from_user(random_number, limit)
        win = compare_results(guess,  interval)
        if win:
            update_score(difficulty)
        print_result(win, secret_number)
        again = continue_play()
        if again:
            restart_main()
        else:
            return
    else:
        print("Unable to play the game due to currency rate retrieval failure.")


def get_money_interval(difficulty, exchange_sum):
    acceptable_interval = 10 - difficulty
    lower_interval = exchange_sum - acceptable_interval
    higher_interval = exchange_sum + acceptable_interval
    return lower_interval, higher_interval
