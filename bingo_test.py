"""Unit tests for bingo"""

import math
from random import choice
from string import ascii_letters
from urllib.parse import urlencode
import unittest
from bingo import Bingo

def bingo_double(title='hello', free_square='free', exclamation='yay',
                 length=30) -> Bingo:
    """Returns a test double with a random word list"""
    words = [''.join(choice(ascii_letters) for _ in range(2)) for _ in range(length)]
    return Bingo(title=title, free_square=free_square, exclamation=exclamation,
                 terms=words)

class TestBingo(unittest.TestCase):
    """Unit tests for the Bingo class"""

    def test_combinations(self):
        """Tests for Bingo.combinations()"""
        test_case = bingo_double()
        expected = math.comb(test_case.size(), 24)
        self.assertEqual(expected, test_case.combinations())

    def test_permutations(self):
        """Tests for Bingo.permutations()"""
        test_case = bingo_double()
        expected = math.perm(test_case.size(), 24)
        self.assertEqual(expected, test_case.permutations())

    def test_pick_chance(self):
        """Tests for Bingo.pick_chance()"""
        size = 30
        expected_chance = 24 / size
        test_case = bingo_double(length=size)
        self.assertEqual(expected_chance, test_case.pick_chance())
        # If less than 24 options, the probabilty of being picked is 1
        test_case = bingo_double(length=5)
        expected_chance = 1
        self.assertEqual(expected_chance, test_case.pick_chance())

    def test_size(self):
        """Tests for Bingo.size()"""
        test_case = bingo_double(length=7)
        self.assertEqual(test_case.size(), 7)

    def test_to_url(self):
        """Tests for Bingo.to_url()"""
        test_case = Bingo(title='hello', free_square='free', exclamation='yay!',
                          terms=['hello', 'world'])
        expected = 'https://www.buzzwordbingogame.com/cards/custom/?' + urlencode({
            'title': 'hello',
            'free_square': 'free',
            'exclamation': 'yay!',
            'terms': '\n'.join(['hello', 'world'])
        })
        self.assertEqual(test_case.to_url(), expected)
