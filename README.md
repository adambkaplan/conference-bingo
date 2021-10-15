# Conference Bingo

Generate bingo cards for your favorite tech conference!

# Try it!

1. Create a YAML file with your board name, free space text, terms, and the header `!Bingo`.
   Be sure to include at least 24 terms for the standard 5x5 board.

```yaml
!Bingo
title: Tech Conference
free_square: FREE
exclamation: Bingo!
terms:
- Computers
- Internet
- Crypto
- Hybrid Cloud
...
```

2. Run the script:

```
$ python script.py --file /path/to/my/bingo.yaml
```