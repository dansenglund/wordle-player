from collections import defaultdict

class Guesser:
    def __init__(self, valid_words, valid_guesses):
        """
        valid_words: a set of words that could be the answer
        valid guesses: a set of words that are valid guesses. A superset of wordlist
        """
        self.words = valid_words
        self.guesses = valid_guesses
        self.freqs, self.idxed_freqs = Guesser.get_letter_frequencies(self.words)
        self.probs = Guesser.hist_to_probs(self.freqs)
        self.idxed_probs = {key: Guesser.hist_to_probs(value) for key, value in self.idxed_freqs.items()}


    def filter_factor(self, char, idx, is_first):
        """
        Compute the factor by which guessing this character at this idx
        """
        # prob word has char at this idx * % of words remaining in this case
        case1 = self.idxed_probs[idx][char] * self.idxed_probs[idx][char]

        # prob word has char at any other idx
        



    def get_guess():
        pass

    def get_letter_frequencies(word_list):
        total_counts = defaultdict(int)
        indexed_counts = defaultdict(lambda: defaultdict(int))
        for word in word_list:
            for idx, char in enumerate(word):
                total_counts[char] += 1
                indexed_counts[idx][char] += 1
        return dict(total_counts), dict({key: dict(value) for key, value in indexed_counts.items()})

    def hist_to_probs(hist):
        return {key: value / sum(hist.values()) for key, value in hist.items()}

def strip_newlines(wordlist):
    return [w.strip() for w in wordlist]

if __name__ == "__main__":
    with open('wordlist.txt', 'r') as file:
        words = set(strip_newlines(file.readlines()))
    with open('allowed_guesses.txt', 'r') as file:
        guesses = set(strip_newlines(file.readlines())).union(words)
    guesser = Guesser(words, guesses)