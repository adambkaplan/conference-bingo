# bingo.py
# Inputs
# -f, --file: board configuration file
# Output - html link to https://www.buzzwordbingogame.com/

import click
import yaml
from yaml.error import YAMLError
from urllib.parse import urlencode

class Bingo(yaml.YAMLObject):

    yaml_loader = yaml.SafeLoader
    yaml_tag = '!Bingo'

    def __init__(self, title, free_square, exclamation, terms) -> None:
        self.title = title
        self.free_square = free_square
        self.exclamation = exclamation
        self.terms = terms
    
    def __repr__(self) -> str:
        return '{0}(title={1},free_space={2},exclamation={3},terms={4})'.format(
            self.__class__.__name__, self.title, self.free_square, self.exclamation, self.terms)
    
    def to_url(self) -> str:
        as_dict = {
            'title': self.title,
            'free_square': self.free_square,
            'exclamation': self.exclamation,
            'terms': '\n'.join(self.terms)
        }
        return "https://www.buzzwordbingogame.com/cards/custom/?" + urlencode(as_dict)


def parse_file(file):
    with open(file, "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except YAMLError as err:
            print("Failed to parse YAML: " + err)
            return
        return config

@click.command()
@click.option('--file', help='file that contains the bingo board definition')
def bingo(file):
    print('Generating bingo board from ' + file)
    config = parse_file(file)
    print(config)
    bingo = Bingo(config.title, config.free_square, config.exclamation, config.terms)
    print('Your bingo board url:')
    print(bingo.to_url())

if __name__ == '__main__':
    bingo()
