"""Practicing Functions to use on Dictionaries and to Test."""
__author__ = "730480319"


def invert(first: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, return the values backwards."""
    backwards: dict[str, str] = {}
    key_list: list[str] = []
    for key in first:
        if first[key] in key_list:
            # if there is already that value present after it was inverted, then raise a KeyError("Duplicate Key Error.")
            raise KeyError("Duplicate Key Error.")
        else:
            # if there are no repeats, add the new key 
            key_list.append(first[key])
    for key in first:
        # switch the old key with the new value by using temporary variables
        val = backwards[key]
        key_list[val] = key
    return backwards


def favorite_color(colors: dict[str, str]) -> str:
    """Given a dictionary of names and colors, return which color as the most 'votes'."""
    count: dict[str, int] = {}
    key_list: list[str] = []
    for key in colors:
        if colors[key] not in key_list:
            # if key is not in key list, add it to the key list and the dictionary
            count[colors[key]] = 1
            key_list.append(colors[key])
        else:
            # if not new then just add 1
            count[colors[key]] += 1
    max_count: int = 0 
    max_color: str = ""
    for key in count:
        # if the amount of times the color occurs is mor ethan the max count then the max count is reassigned and the 'fav' color changes.
        if count[key] > max_count:
            max_count = count[key]
            max_color = key
    return max_color


def count(counter: list[str]) -> dict[str, int]:
    """Given a list of strings, count how many times each string occurs and return a dictionary."""
    counts: dict[str, int] = {}
    for i in counter:
        if i in counter:
            # if there is a new word, add it to the new dictionary and assign it to 1 
            counts[i] += 1
        else:
            counts[i] = 1
    return counts