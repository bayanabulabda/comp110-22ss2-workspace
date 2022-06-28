"""Combining learned concepts in week 1 by programming one-shot-wordle."""
__author__ = "730480319"
# globals and variables
secret = "python"
len_secret = len(secret)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# asks for guess to check the length of the secret word
guess = input(f"What is your {len_secret}-letter guess? ")
while len(guess) != len(secret):
    guess = input(f"That was not {len_secret} letters! Try again: ")

i = 0
emoji = ("")
while i < len_secret: 
    if guess[i] == secret[i]:  # guess and secret have the same letter at the same index
        emoji = (f"{emoji}{GREEN_BOX}")
    else:
        other = False
        j = 0       
        while not other and j < len_secret: 
            if guess[i] == secret[j]:  # guess and secret have the same letter at different indeces
                other = True
            j = j + 1  # to make sure it is not an infinite loop 
        if other:
            emoji = (f"{emoji}{YELLOW_BOX}")
        else:
            emoji = (f"{emoji}{WHITE_BOX}")
    i = i + 1  # to make sure it is not an infinite loop 
# writes out the results of the game
print(emoji)
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")