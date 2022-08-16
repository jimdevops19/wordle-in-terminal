import random
import sys
from valid_words import valid_words


#Comments Added
CHOSEN_WORD = random.choice(valid_words)
GUESSES_COUNT = 6


class Color:
    PREFIX = '\033'
    BASE = "\033[0m"
    GREY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    PERSISTENT_COLORS = [RED, GREEN]

class GuessWord:
    counter = 1
    wordles = []
    alphabet = {
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
    }
    def __init__(self, w_str:str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)
        self.post_guess_w_str = ""
        self.wordleArr = [ltr for ltr in CHOSEN_WORD]

    def jump_turn(self):
        GuessWord.counter += 1

    def is_valid(self):
        return self.w_str in valid_words

    def apply_greens(self):
        for i, _ in enumerate(self.w_chars):
            actual_char = CHOSEN_WORD[i]
            guessed_char = self.w_chars[i]
            if actual_char == guessed_char:
                colored_char = f"{Color.GREEN}{actual_char}{Color.BASE}"
                self.w_chars[i] = colored_char
                self.edit_alphabet(actual_char, colored_char)
                self.wordleArr[i] = "_"

    def apply_yellows(self):
        self.tempArr = self.wordleArr
        for i, _ in enumerate(self.w_chars):
            guessed_char = self.w_chars[i]
            for j, _ in enumerate(self.tempArr):
                if guessed_char == self.tempArr[j]:
                    colored_char = f"{Color.YELLOW}{guessed_char}{Color.BASE}"
                    self.w_chars[i] = colored_char
                    self.edit_alphabet(guessed_char, colored_char)
                    self.tempArr[j] = "_"
                else:
                    colored_char = f"{Color.RED}{guessed_char}{Color.BASE}"
                    self.edit_alphabet(guessed_char, colored_char)

    def edit_alphabet(self, k, v):
        if k not in GuessWord.alphabet.keys():
            # A new key value pair is being added.
            return

        # Do not modify key value pairs that are already green or red
        older_value = GuessWord.alphabet.get(k, "")
        modify_color = True
        for c in Color.PERSISTENT_COLORS:
            if c in older_value:
                modify_color = False

        if modify_color:
            GuessWord.alphabet[k] = v

    def apply_guesses(self):
        self.apply_greens()
        self.apply_yellows()
        self.post_guess_w_str = "".join(self.w_chars)
        GuessWord.wordles.append(self.post_guess_w_str)
        print(self.post_guess_w_str)

    def check_perfect_guess(self):
        if self.w_str == CHOSEN_WORD:
            print(f"Congratulations! You beat Wordle in {GuessWord.counter} guesses")
            for element in GuessWord.wordles:
                print(element)
            sys.exit(0)

    def check_game_loss(self):
        if GuessWord.counter == GUESSES_COUNT + 1:
            print(f"You lost the game. The word was {CHOSEN_WORD}")
            sys.exit(0)
