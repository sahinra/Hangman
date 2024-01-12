

def get_all_words():
    countries_capitals = []
    f = open('countries-and-capitals.txt', 'r+')
    for line in f.readlines():
        countries_capitals.append(line)
    f.close()
    return countries_capitals


def get_countries_and_capitals():
    all_words = get_all_words()
    countries = []
    capitals = []
    for item in all_words:
        item_list = "".join(item.split()).split("|")
        countries.append(item_list[0])
        capitals.append(item_list[1])
    return countries, capitals


def set_the_difficulty():
    levels = [1, 2, 3]
    difficulty_level = 1
    try:
        difficulty_level = int(input("Please type the difficulty level. 1-Easy, 2-Medium, 3-Hard "))
        while difficulty_level not in levels:
            difficulty_level = int(input("Please type a valid difficulty level. 1-Easy, 2-Medium, 3-Hard "))
        return difficulty_level
    except ValueError:
        print("Not a number. Your difficulty level is 1")
        return 1


def get_words_by_difficulty_level(difficulty, countries, capitals):
    if difficulty == 1:
        print("DIFFICULTY LEVEL 1 (COUNTRIES)")
        return countries
    elif difficulty == 2:
        print("DIFFICULTY LEVEL 2 (CAPITALS)")
        return capitals
    elif difficulty == 3:
        print("DIFFICULTY LEVEL 2 (COUNTRIES AND CAPITALS)")
        return countries + capitals




# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level


# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5 # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
already_tried_letters = [] # this list will contain all the tried letters


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.



# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4


def main():
    countries, capitals = get_countries_and_capitals()
    selected_difficulty = set_the_difficulty()
    words_by_level = get_words_by_difficulty_level(selected_difficulty, countries, capitals)
    print(words_by_level)


if __name__ == "__main__":
    main()