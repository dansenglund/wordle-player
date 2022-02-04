# wordle-player

An attempt to create a perfect Wordle player based on analyzing the underlying wordlist

Simulating different strategies:

- True-optimal (from https://medium.com/@tglaiel/the-mathematically-optimal-first-guess-in-wordle-cbcb03c19b0a)
- Win rate = 100%
- 3.49

Pseudo-optimal, just valid answers

- {4: 911, 6: 62, 5: 283, 3: 920, 2: 120, 7: 14, 8: 4, 1: 1}
- Win rate = 99.2%
- Avg: 3.69

Guess “arose” and then random

- {5: 432, 4: 873, 3: 715, 8: 9, 6: 148, 7: 28, 2: 107, 9: 2, 1: 1}
- Win rate = 98.3%
- Overall average attempts: 3.968034557235421

Full random:

- {4: 879, 5: 556, 3: 577, 2: 94, 6: 161, 7: 34, 1: 2, 8: 12}
- Win rate = 98.0%
- Overall average attempts: 4.111015118790497
