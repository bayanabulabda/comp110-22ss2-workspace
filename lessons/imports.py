"""Examples of importing in python."""


from lessons import helpers
from lessons import helpers as hp

from lessons.helpers import powerful, THE_ANSWER



def main() -> None:
    """Entrypoint of a program."""
print(helpers.powerful(2, 4))
print(f"The answer: {helpers.THE_ANSWER}")

if __name__ == "__main__":
    main()