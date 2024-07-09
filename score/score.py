from utils import wright_file, file_path, error, read_file


def update_score(difficulty):
    add_score(difficulty, file_path, error)


def add_score(difficulty, file_path, error):
    points_of_winning = (difficulty * 3) + 5
    summ = int(read_file(file_path, error))
    if summ == error:
        print(f"Could not read/write the file. ERROR {error}")
    summ += points_of_winning
    result = int(wright_file(file_path, summ, error))
    if result == error:
        print(f"Could not read/write the file. ERROR {error}")
