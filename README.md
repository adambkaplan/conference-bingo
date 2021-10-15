# Conference Bingo

Generate bingo cards for your favorite tech conference!

## Try it!

1. Install [Python](https://www.python.org/downloads/) for your desired environment.

2. Clone this repository:

```sh
$ git clone https://github.com/adambkaplan/conference-bingo.git
$ cd conference-bingo
```

3. Install the dependencies (ideally using venv):

```sh
$ python -m venv env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
```

4. Create a YAML file with your board name, free space text, terms, and the header `!Bingo`.
   Be sure to include at least 24 terms for the standard 5x5 board.

```yaml
!Bingo
title: Tech Conference
free_square: FREE
exclamation: Bingo!
terms:
- Computers
- Crypto(currency)
- Hybrid Cloud
- Internet
...
```

5. Run the script:

```sh
$ python script.py --file /path/to/my/bingo.yaml
```

## Conferences

Use this repository to collaborate on Bingo word lists for your favorite tech conferences.
Each conference should have its own top-level directory, with subdirectories for a particular year and location.

## Contributing

Got a conference you would like to add?
Pull requests for new conferences or improvements to the `bingo.py` script are welcome!
See the [contributor guide](CONTRIBUTING.md) for more information.

## License

Copyright 2021 Adam B Kaplan
MIT License - see [LICENSE](LICENSE) for full information.