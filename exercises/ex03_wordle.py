"""Wordle with a specific number of tries."""
__author__: "730480319" 

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, letter: str) -> bool:
    """Check if the letter is in the secret word."""
    assert len(letter) == 1
    i = 0
    while i < len(word):
        if word[i] == letter:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Compares the guess with the secret word and outputs coolor coded emojis."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    i = 0
    result = ""
    while i < len(secret):
        if secret[i] == guess[i]:
            result = (f"{result}{GREEN_BOX}")
        else:
            if contains_char(secret, guess[i]):
                result = (f"{result}{YELLOW_BOX}")
            else:
                result = (f"{result}{WHITE_BOX}")
        i = i + 1
    return result

def input_guess(length: int) -> str:
    """Keeps track of the secret words length."""
    guess = input(f"What is your {length}-letter guess? ")
    while len(guess) != length:
        guess = input(f"That was not {length} letters! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop"""
    turns = 0
    won = False
    secret = "codes"
    while not won and turns < 6:
        print(f"=== Turn {turns + 1}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turns +1}/6 turns!")
            won = True
        turns = turns + 1
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()