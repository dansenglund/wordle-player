from collections import defaultdict

class Guesser:
    def __init__(self, word_list, allowed_words):
        pass

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


