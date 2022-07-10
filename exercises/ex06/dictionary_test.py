"""Testing the Functions of the Dictionary file in ex06."""
__author__ = "730480319"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count
import pytest


def test_invert_repeat_keys() -> None:
    """Repeat keys should raise a KayError."""
    with pytest.raises(KeyError):
        my_dictionary = {'Bella': 'Hadid', 'Gigi': 'Hadid'}
        invert(my_dictionary)


def test_invert_one_pair() -> None:
    """One key-value pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert() -> None:
    """Longer dictionary."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_favorite_color() -> None:
    """Normal use."""
    assert favorite_color({"Bayan": "Green", "Malak": "Purple", "Mama": "Purple"}) == "Purple"


def test_favorite_color_same() -> None:
    """If the colors are at a tie, return the first one in the dict."""
    assert favorite_color({"Bayan": "Green", "Malak": "Purple"}) == "Green"


def test_favorite_color_pt_2() -> None:
    """Normal use pt 2."""
    assert favorite_color({"Bayan": "Green", "Malak": "Purple", "Mama": "Purple", "Leith": "Blue"}) == "Purple"


def test_count() -> None:
    """Normal Use."""
    assert count(["Malak", "Bayan", "Ahmad", "Ahmad"]) == {"Malak": 1, "Bayan": 1, "Ahmad": 2}


def test_count_empty_list() -> None:
    """Empty list should return a border."""
    assert count([]) == {}


def test_count_again() -> None:
    """Normal Use again."""
    assert count(["Malak", "Bayan", "Ahmad", "Leith"]) == {"Malak": 1, "Bayan": 1, "Ahmad": 1, "Leith": 1}