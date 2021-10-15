"""Unit tests for bingo"""

from urllib.parse import urlencode
import unittest
from bingo import Bingo

class TestBingo(unittest.TestCase):
    """Unit tests for the Bingo class"""

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
