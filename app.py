from games.guess_game import play_guess_game
from games.currency_roulette_game import play_currency_roulette_game
from games.memory_game import play_memory_game
from utils import cls, validate_input


def welcome():
    cls()
    username = input("Enter your name\t")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def start_play():
    game = None
    difficulty = None
    list_games = ["1.  Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.",
                  "2.  Guess Game - guess a number and see if you chose like the computer. ",
                  "3.  Currency Roulette - try and guess the value of a random amount of USD in ILS ",
                  ]
    for lst in list_games:
        print(lst)
    check = True
    while check:
        game = input("Please choose a game to play: \t")
        if validate_input(game, len(list_games)):
            continue
        else:
            while check:
                difficulty = input("Select a difficulty level between 1 and 5: \t")
                if validate_input(difficulty, 5):
                    continue
                else:
                    game = int(game)
                    difficulty = int(difficulty)
                    check = False
    play_game(game, difficulty)


def play_game(game, difficulty):
    match game:
        case 1:
            play_memory_game(difficulty)
        case 2:
            play_guess_game(difficulty)
        case 3:
            play_currency_roulette_game(difficulty)
