import hangman


def test_word_fully_match():
    # arrange
    word = "hello"
    letters = set(word)
    # act
    res = hangman.word_fully_match(word, letters)
    # assert
    assert res is True


def test_word_fully_match_with_empty_set():
    # arrange
    word = "hello"
    letter = set()
    # act
    res = hangman.word_fully_match(word, letter)
    # assert
    assert res is False


def test_word_fully_match_with_uppercase_word():
    # arrange
    word = "GREAT"
    letters = set(word.lower())
    # act
    res = hangman.word_fully_match(word, letters)
    # assert
    assert res is True




