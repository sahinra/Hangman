import random


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
        item_list = [h.strip() for h in item.split("|")]
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


def set_lives_by_difficulty_level(difficulty):
    total_lives = 7
    if difficulty == 1:
        total_lives = 7
    elif difficulty == 2:
        total_lives = 5
    elif difficulty == 3:
        total_lives = 3
    return total_lives


def get_random_word(word_list):
    return random.choice(word_list)


def display_word(word, found_list):
    updated_word = []
    for letter in word:
        if letter.lower() in found_list:
            updated_word.append(letter)
        else:
            updated_word.append("_")
    print("".join(updated_word))


def word_fully_match(actual_word, letter_set):
    for aw in actual_word:
        if aw.lower() not in letter_set:
            return False
    return True


def try_to_guess(word_to_guess, found_letters, incorrect_letters, lives):
    print("YOUR WORD")
    display_word(word_to_guess, found_letters)

    while not word_fully_match(word_to_guess, found_letters):
        letter = input("Type a letter - ")

        while len(letter) > 1:
            if letter == "quit":
                print("Goodbye! Hope to see you in next games :)")
                exit()
            letter = input("Please write a letter - ")

        if letter.lower() in word_to_guess or letter.upper() in word_to_guess:
            if letter in found_letters:
                print(f"You found {letter}! Try another letter - ")
            else:
                found_letters.add(letter.lower())
        elif not letter.isalpha():
            print("Wrong type! Please provide a letter")
        else:
            if letter.lower() in incorrect_letters:
                print("It's already wrong.")
            else:
                incorrect_letters.add(letter.lower())
                print("Wrong guess! Previous wrong letters are:")
                print(' '.join(incorrect_letters))
                lives -= 1
                if lives <= 0:
                    print("YOU LOST THE GAME :(")
                    exit()
            print(f"You have {lives} lives left")

        display_word(word_to_guess, found_letters)

    print("YOU WON THE GAME!! :)")
    display_word(word_to_guess, found_letters)
    print("Goodbye! Hope to see you in next games :)")
    exit()


def main():
    print(r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      
    """)
    revealed_letters = set()
    wrong_letters = set()

    countries, capitals = get_countries_and_capitals()

    selected_difficulty = set_the_difficulty()
    words_by_level = get_words_by_difficulty_level(selected_difficulty, countries, capitals)
    lives = set_lives_by_difficulty_level(selected_difficulty)

    word_to_guess = get_random_word(words_by_level)
    print(word_to_guess)
    try_to_guess(word_to_guess, revealed_letters, wrong_letters, lives)


if __name__ == "__main__":
    main()