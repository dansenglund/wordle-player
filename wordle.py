import random

class Wordle:
    def __init__(self, allowed_answers , allowed_guesses):
        self.all_answers = allowed_answers
        self.all_guesses = allowed_guesses

    def start(self):
        while True:
            answer = random.choice(tuple(self.all_answers))
            game = self.Game(answer, self.all_guesses)
            game.start()


    class Game:
        def __init__(self, answer, wordlist):
            self.answer = answer
            self.wordlist = wordlist

        def start(self):
            while True:
                guess = input()
                if guess == "surrender":
                    print(self.answer)
                    break
                print(self.checkGuess(guess))
                if guess == self.answer:
                    print("You Won!")
                    break

        def checkGuess(self, guess):
            if len(guess) != 5:
                return "Must be a 5 letter word"
            if guess not in self.wordlist:
                return "That is not a word"

            result = ""
            for i, letter in enumerate(guess):
                if letter == self.answer[i]:
                    result += "O"
                elif letter in self.answer:
                    result += "?"
                else:
                    result += "_"
            return result




def strip_newlines(wordlist):
    return [w.strip() for w in wordlist]

if __name__ == "__main__":
    with open('wordlist.txt', 'r') as file:
        words = set(strip_newlines(file.readlines()))
    with open('allowed_guesses.txt', 'r') as file:
        guesses = set(strip_newlines(file.readlines())).union(words)
    wordle = Wordle(words, guesses)
    wordle.start()