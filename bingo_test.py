import unittest
from bingo import Bingo
from urllib.parse import urlencode

class TestBingo(unittest.TestCase):

    def test_to_url(self):
        test_case = Bingo(title='hello', free_square='free', exclamation='yay!', terms=['hello', 'world'])
        expected = 'https://www.buzzwordbingogame.com/cards/custom/?' + urlencode({
            'title': 'hello',
            'free_square': 'free',
            'exclamation': 'yay!',
            'terms': '\n'.join(['hello', 'world'])
        })
        self.assertEqual(test_case.to_url(), expected)
