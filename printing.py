from reports import *


def decor(func):
    """ Add 1st and last line to what the function returns. """
    def wrap():
        print("@@@ STATISTICS REPORT START @@@\n")
        func()
        print("@@@ STATISTICS REPORT FINISH @@@\n")
    return wrap


@decor
def print_all():
    """ Print what the function returns in seperate lines. """
    print("1. Number of games is:\n\n", count_games("game_stat.txt"), "\n")
    print("2. There is a game from a given year on the list:\n\n", decide("game_stat.txt", 2004), "\n")
    print("3. The latest game on the list is:\n\n", get_latest("game_stat.txt"), "\n")
    print("4. Number of games from the list in the given genre is:\n\n", count_by_genre("game_stat.txt", "rpg"), "\n")
    print("5. List spot of the given game is:\n\n", get_line_number_by_title("game_stat.txt", "counter-strike"), "\n")
    print("6. Alphabetically sorted games:\n\n", "\n ".join(sort_abc("game_stat.txt")), "\n")
    print("7. List of genres:\n\n", "\n ".join(get_genres("game_stat.txt")), "\n")
    print("8. Top sold FPP game premiered in:\n\n", when_was_top_sold_fps("game_stat.txt"), "\n")


print_all()
