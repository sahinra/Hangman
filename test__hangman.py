import pytest

import hangman
from hangman import word_fully_match


class Tests:
    def test_word_fully_match(self):
        # arrange
        word = "hello"
        letters = set()
        letters.add("h")
        letters.add("e")
        letters.add("l")
        letters.add("o")
        # act
        res = hangman.word_fully_match(word, letters)
        # assert
        assert res is True

    def test_word_fully_match_with_empty_set(self):
        # arrange
        word = "hello"
        letter = set()
        # act
        res = hangman.word_fully_match(word, letter)
        # assert
        assert res is False

    def test_word_fully_match_with_uppercase_word(self):
        # arrange
        word = "GREAT"
        letters = set()
        letters.add("t")
        letters.add("g")
        letters.add("e")
        letters.add("a")
        letters.add("r")
        # act
        res = hangman.word_fully_match(word, letters)
        # assert
        assert res is True




