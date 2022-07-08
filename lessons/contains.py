"""Example of writing a function to process a list"""
__author__ = "730480319"

def main() -> None:
    """Body of program."""
    names: list[str] = ["Bayan", "Malak", "Ahmad", "Leith"]
    print(contains("Entisar", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True iff needle is found in the haystack, else False."""
    # Move through each item in list until needle is found
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1
        
    return False
      

if __name__ == "__main__":
    main()