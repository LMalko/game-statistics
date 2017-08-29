from reports import *

with open("statistics.txt", 'w', encoding='utf-8') as statistics_export:
    # Take the values that are being returned by functions in reports.py.
    # Export each one of them to seperate line in .txt file.
    statistics_export.write(str(count_games("game_stat.txt")) + "\n")
    statistics_export.write(str(decide("game_stat.txt", 2000)) + "\n")
    statistics_export.write(get_latest("game_stat.txt") + "\n")
    statistics_export.write(str(count_by_genre("game_stat.txt", "rpg")) + "\n")
    statistics_export.write(str(get_line_number_by_title("game_stat.txt", "counter-strike")) + "\n")
    statistics_export.write(str(sort_abc("game_stat.txt")) + "\n")
    statistics_export.write(str(get_genres("game_stat.txt")) + "\n")
    statistics_export.write(str(when_was_top_sold_fps("game_stat.txt")) + "\n")
