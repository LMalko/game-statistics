def count_games(file_name):
    ''' Count games in the file. '''
    while True:
        try:
            with open(file_name, "r", encoding='utf-8') as file_name:
                return len(file_name.readlines())
        except FileNotFoundError:
            return "No such file."


def decide(file_name, year):
    ''' Evaluate if there is a game from this year. '''
    while True:
        try:
            with open(file_name, "r", encoding='utf-8') as file_name:
                file_name = file_name.readlines()
                # We assign only the 3rd column to the list, in case there are games such as Anno 2270 or FM 2017.
                years_list = []
                for i in file_name:
                    years_list.append(i.split("\t")[2])
                if str(year) in years_list:
                    return True
                else:
                    return False
        except FileNotFoundError:
            return "No such file."


def get_latest(file_name):
    ''' Return newest game from the list. '''
    while True:
        try:
            with open(file_name, "r", encoding='utf-8') as file_name:
                # Assign each line as an element to the list.
                file_name = file_name.readlines()
                years_list = []
                # Assign values from 3rd column to the list.
                for i in file_name:
                    years_list.append(i.split("\t")[2])
                # Assign the latest year to a variable.
                latest_year = max(years_list)
                # Return the title with the same index position as the value of "latest_year" variable.
                latest_game_index_number = years_list.index(latest_year)
                latest_game_details = file_name[latest_game_index_number]
                latest_game_name = latest_game_details.split("\t")[0]
                return latest_game_name
        except FileNotFoundError:
            return "No such file."


def count_by_genre(file_name, genre):
    ''' Return number of games from genre. '''
    while True:
        try:
            with open(file_name, "r", encoding='utf-8') as file_name:
                file_name = file_name.readlines()
                genre_list = []
                for i in file_name:
                    # Append values from the 4th column. Use upper() in case someone uses Caps Lock.
                    genre_list.append((i.split("\t")[3].upper()))
                return genre_list.count(genre.upper())
        except FileNotFoundError:
            return "No such file."


def get_line_number_by_title(file_name, title):
    ''' Return line number by title. '''
    while True:
        try:
            with open(file_name, "r", encoding='utf-8') as file_name:
                file_name = file_name.readlines()
                titles_list = []
                # Append only the 1st value from each element of "file_name" list.
                for i in file_name:
                    titles_list.append((i.split("\t")[0].upper()))
                # Add 1 to disdain [0] position.
                return titles_list.index(title.upper()) + 1
        except FileNotFoundError:
            return "No such file."


def sort_abc(file_name):
    ''' Return alphabetically ordered stats. '''
    while True:
        try:
            with open(file_name, "r", encoding='utf-8') as file_name:
                file_name = file_name.readlines()
                titles_list = []
                for i in file_name:
                    titles_list.append((i.split("\t")[0]))
                # Initiate variable - list that will gather sorted values.
                titles_list_sorted = []
                # Avoid using sort() or sorted().
                # Loop through "titles_list", each time append min value.
                for i in range(len(titles_list)):
                    titles_list_sorted.append(min(titles_list))
                    titles_list.remove(min(titles_list))
                return titles_list_sorted
        except FileNotFoundError:
            return "No such file."


def get_genres(file_name):
    ''' Return alphabetically ordered list of genres. '''
    while True:
        try:
            with open(file_name, "r", encoding='utf-8') as file_name:
                file_name = file_name.readlines()
                genre_list = []
                for i in file_name:
                    genre_list.append((i.split("\t")[3]))
                # Change the list to set to avoid duplicates.
                genre_list = set(genre_list)
                # Use lambda to sort to properly order caps locked values.
                genre_list = sorted(genre_list, key=lambda v: v.upper())
                return genre_list
        except FileNotFoundError:
            return "No such file."


def when_was_top_sold_fps(file_name):
    ''' Return year of the highest selling FPP. '''
    while True:
        try:
            with open(file_name, "r", encoding='utf-8') as file_name:
                file_name = file_name.readlines()
                genre_list = []
                # The loop will return only genres.
                for i in file_name:
                    genre_list.append((i.split("\t")[3]))
                line_numbers = []
                # Assign to variable position of all FPP.
                line_numbers = [i for i, x in enumerate(genre_list) if x == 'First-person shooter']
                # Assign sales list to variable.
                sales_list = []
                for i in line_numbers:
                    # Append only sales from FPP.
                    sales_list.append(file_name[i].split("\t")[1])
                for i in sales_list:
                    # Change all elements to float.
                    sales_list[sales_list.index(i)] = float(i)
                # Assign index position of the highest float to a variable.
                maximum_sale_row_number = sales_list.index(max(sales_list))
                # Return the year value from the index position equal to max sale index position.
                return int(file_name[line_numbers[maximum_sale_row_number]].split("\t")[2])
        except FileNotFoundError:
            return "No such file."
