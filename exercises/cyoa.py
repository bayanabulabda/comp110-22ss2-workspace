"""An adventure game implementing what has been learned so far."""
__author__ = "730480319"

yay_emoji: str = "\U0001F973"
sad_emoji: str = "\U0001F614"
player: str
points: int = 0


def main() -> None:
    """To run the overall game."""
    greet()
    questions()


def greet() -> None:
    """Greeting function!"""
    welcome: str = ("Welcome to Mythology! The game show all about heros, myths and their adventures! This game will be one where we ask you questions and you get points for the right answer!")
    print(f"{welcome}")
    player: str = input("What is your name?")
    print(f"Hello, {player}! Here's your first question.")


def questions() -> None:
    """Body of questions and answers."""
    points: int = 0
    q = ["Who is Percy Jacksons father?", "What is another name for Zeus?", "(Yes/No) Thor is part of Greek Mythology."]
    a = ["Poseidon", "Jupiter", "No"]

    i = 0
    while i < len(q): 
        print(q[i])
        guess: str = input("")
        if guess == a[i]:
            print(f"Correct! {yay_emoji} Here's your next question.")
            points += 1
            print(f"Your current points are {points}.")
        else:
            print(f"Not quite. Game over {sad_emoji}.")
            print(f"Your current points are {points}.")
            quit()
        i += 1
        if points == 3:
            print(f"Congrats, you win!{yay_emoji}")
    

if __name__ == "__main__":
    main()