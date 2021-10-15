"""This module, when run as a script, generates a custom bingo board URL for
https://www.buzzwordbingogame.com/ from a YAML configuration file.
"""

import sys
from urllib.parse import urlencode
import click
import yaml
from yaml.error import YAMLError

class Bingo(yaml.YAMLObject):
    """Allows for simple serialization of the bingo board YAML, and logic to generate the board
    URL.
    """

    yaml_loader = yaml.SafeLoader
    yaml_tag = '!Bingo'

    def __init__(self, title, free_square, exclamation, terms) -> None:
        self.title = title
        self.free_square = free_square
        self.exclamation = exclamation
        self.terms = terms

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}(title={self.title},free_square={self.free_square}'
            f'exclamation={self.exclamation},terms={self.terms})'
        )

    def to_url(self) -> str:
        """Returns the URL for bingo board"""
        as_dict = {
            'title': self.title,
            'free_square': self.free_square,
            'exclamation': self.exclamation,
            'terms': '\n'.join(self.terms)
        }
        return "https://www.buzzwordbingogame.com/cards/custom/?" + urlencode(as_dict)


def parse_file(file):
    """Parses a YAML file containing the bingo board configuration"""
    with open(file=file, mode="r", encoding='UTF-8') as stream:
        try:
            config = yaml.safe_load(stream)
        except YAMLError as err:
            sys.exit("Failed to parse YAML: " + err)
        return config

@click.command()
@click.option('--file', help='file that contains the bingo board definition')
def bingo(file):
    """Generates a bingo board URL from a provided YAML configuration file"""
    print('Generating bingo board from ' + file)
    config = parse_file(file)
    print(config)
    board = Bingo(config.title, config.free_square, config.exclamation, config.terms)
    print('Your bingo board url:')
    print(board.to_url())

if __name__ == '__main__':
    # click provides the arguments to the bingo function
    # pylint: disable=no-value-for-parameter
    bingo()
