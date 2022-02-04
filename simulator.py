from importlib.metadata import distribution
from guesser import Guesser
from collections import defaultdict

def strip_newlines(wordlist):
    """Strip whitespace from a list of strings"""
    return [w.strip() for w in wordlist]

def load_words():
    with open('wordlist.txt', 'r') as file:
        words = set(strip_newlines(file.readlines()))
    with open('allowed_guesses.txt', 'r') as file:
        guesses = set(strip_newlines(file.readlines())).union(words)
    return words, guesses

def filter_wordlist(guess, answer, wordlist):
    """Given a guessed word and a feedback string, return the filtered wordlist"""
    filtered = list(wordlist)
    for i, letter in enumerate(guess):
        if letter == answer[i]:
            filtered = [word for word in filtered if word[i] == letter]
        elif letter in answer:
            filtered = [word for word in filtered if (letter in word) and word[i] != letter]
        else:
            filtered = [word for word in filtered if letter not in word]
    return set(filtered)

def simulate_pseudooptimal(answer, wordlist, guesslist):
    # print(f"Answer: {answer}, possible answers: {len(wordlist)}")
    guesses = 0
    while len(wordlist) > 0:
        guesses += 1
        guesser = Guesser(wordlist, guesslist)
        guess = guesser.get_guess()
        # guess = guesser.get_random()

        if guess == answer:
            return guesses
        else:
            wordlist = filter_wordlist(guess, answer, wordlist)
        # print(f"Guess: {guess}, remaining possibilities: {len(wordlist)}")
        

    raise Exception("Oops ran out of words somehow")

if __name__ == '__main__':
    words, guesses = load_words()

    all_attempts = []
    total_guesses = 0
    for word in words:
        attempts = simulate_pseudooptimal(word, words, guesses)
        total_guesses += attempts
        print(word, attempts)
        all_attempts.append((word, attempts))

    distribution = defaultdict(int)
    wins = 0
    for word, attempts in all_attempts:
        distribution[attempts] += 1
        # print(word, attempts)
        if attempts <= 6:
            wins += 1
    print(distribution)
    print(f"Win rate = {100 * wins / len(all_attempts)}%")

    print(f"Overall average attempts: {total_guesses / len(words)}")
