"""Defining the Functions."""
__author__ = "730480319"

def only_evens(int_list: list[int]) -> list[int]:
    """With a given list, return a new list with only the even numbers."""
    result: list[int] = []
    i: int = 0
    while i < len(int_list):
        if int_list [i] % 2 == 0:
            result.append(int_list[i])
        i += 1
    return result


def is_equal(int_list1: list[int], int_list2: list[int]) -> list[int]:
    """To compare two lists by their indeces."""
    if int_list1 == int_list2:
        return True
    else:
        return False
    

def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Return part of the list when given a start index and an end index."""
    result: list[int] = []
    if start < 0:
        start =0
    if end > len(a_list):
        end = len(a_list)
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return result
    i: int = start
    while i < end:
        result.append(a_list[i])
        i += 1
    return result

