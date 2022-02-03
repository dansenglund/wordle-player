WORDLENGTH = 5

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
        
    def char_filter_factor(self, char, idx, is_first):
        """
        Compute the factor by which guessing this character at this idx filters
        """
        # Case 1: char at index
        case1 = self.idxed_probs[idx][char] * (1 - self.idxed_probs[idx][char])
        
        # TODO: this isn't exact as it double counts in cases where characters appear multiple times but probably good enough
        case2 = 0
        case3 = 0
        if is_first:
            # Case 2: char elsewhere in word
            prob_at_other = (5 * self.probs[char] - self.idxed_probs[idx][char]) # All probs normalized by same factor
            case2 = prob_at_other * (1 - prob_at_other)

            # Case 3: char elsewhere in word
            prob_not_in = 1 - self.probs[char]
            case3 = prob_not_in * (1 - prob_not_in)

        filter_factor = case1 + case2 + case3
        return (1 - filter_factor)
  
    def word_filter_factor_naive(self, word):
        """Compute the filter factor of a word. Naively the product of the filter factors (with special handling for duplicate chars"""
        accumulator = 1
        for idx, char in enumerate(word):
            is_first = word.index(char) == idx
            factor = self.char_filter_factor(char, idx, is_first)
            accumulator *= factor
        return accumulator
    
    def get_guess(self):
        return max(self.words, key=lambda word: -1 * self.word_filter_factor_naive(word))

    def get_letter_frequencies(word_list):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        total_counts = {char : 0 for char in alphabet}
        indexed_counts = {}
        for i in range(WORDLENGTH):
            indexed_counts[i] = dict(total_counts) # Same structure as total counts
        for word in word_list:
            for idx, char in enumerate(word):
                total_counts[char] += 1
                indexed_counts[idx][char] += 1
        return total_counts, indexed_counts

    def hist_to_probs(hist):
        return {key: value / sum(hist.values()) for key, value in hist.items()}

def strip_newlines(wordlist):
    return [w.strip() for w in wordlist]

if __name__ == "__main__":
    with open('wordlist.txt', 'r') as file:
        words = set(strip_newlines(file.readlines()))
    with open('allowed_guesses.txt', 'r') as file:
        guesses = set(strip_newlines(file.readlines())).union(words)
    print(Guesser(words, guesses).get_guess())