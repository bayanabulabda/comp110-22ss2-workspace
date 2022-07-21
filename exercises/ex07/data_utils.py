"""Dictionary related utility functions."""
<<<<<<< HEAD
__author__ = "730480319"

from csv import DictReader


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Open a file and read it as rows."""
    result: list[dict[str, str]] = []
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result 


def column_values(tbl: list[dict[str, str]], col: str) -> list[str]:
    """Given a column, return a list of strings of the content in the columns."""
    result: list[str] = []
    for row in tbl:
        item: str = row[col]
        result.append(item)
    return result


def columnar(tbl: list[dict[str, str]]) -> dict[str, list[str]]:
    """Switch from a table represented by rows to represented by columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = tbl[0]
    for column in first_row:
        result[column] = column_values(tbl, column)
    return result


def head(col_tbl: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Given the first thing of rows, produce a column based table."""
    result: dict[str, list[str]] = {}
    i: int = 0  # To count the rows that are being added as the program is looping.
    for col in col_tbl:
        max_rows = len(col_tbl[col])
        if num_rows > max_rows:
            num_rows = max_rows
        row: list[str] = []  # Empty list used to add the values from the rows before adding it to the table.
        while i < num_rows:
            row.append(col_tbl[col][i])
            i += 1 
        result[col] = row
        i = 0  # Reset the counter
    return result


def select(tbl: dict[str, list[str]], name_col: list[str]) -> dict[str, list[str]]:
    """Given a subset of the original columns, return a new column based table."""
    result: dict[str, list[str]] = {}
    for col in name_col:
        result[col] = tbl[col]
    return result 


def concat(tbl_1: dict[str, list[str]], tbl_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Given two tables, combine them and return as a single table."""
    result: dict[str, list[str]] = {}
    for col in tbl_1: 
        result[col] = tbl_1[col]

    for col in tbl_2:
        if col in result:
            result[col] += tbl_2[col]
        else: 
            result[col] = tbl_2[col]
    return result


def count(freq: list[str]) -> dict[str, int]:
    """Count how many times a value has appearead in the list."""
    result: dict[str, int] = {}
    for i in freq:
        if i in result:  # When an item is found in the dict, add 1 to count
            result[i] += 1
        else:  # Item not found in the dict, so assign it 1
            result[i] = 1
    return result
=======

__author__ = ""

# Define your functions below
>>>>>>> 557f419c9c715d5f240260899912db16331a74ae
