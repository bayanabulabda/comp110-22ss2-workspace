"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730480319"


class Simpy:
    """Simpy object."""

    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize a new Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """Will be called when a Simpy object is converted to a string."""
        return f"Simpy({self.values}"

    def fill(self, value: float, times: int) -> None:
        """Fill our values array by mutating object called on."""
        # Start with an empty values list
        self.values = []
        # Loop for 'times' number of times
        i: int = 0
        while i < times:
            #  Appends value parameter to the values arry 
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in a range of values."""
        # Start with an empty values list
        self.values = []
        # Be sure step is not 0.0 asserting
        assert step != 0.0
        # When step is positive: 
        if step > 0.0:
            # Initialize next value to start
            next_value: float = start
            # While next value is less than stop vlaue
            while next_value < stop:
                # Add next value to values list 
                self.values.append(next_value)
                # Update next value by adding the step to it 
                next_value += step
        # else TODO: handle the negative step 
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step
    
    def sum(self) -> float: 
        """Delegate this algo to the built-in sum function."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for exponentation."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for values in self.values:
                result.values.append(values ** rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result 

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for ==."""
        result: list[bool] = []
        lhs: list[float] = self.values
        rhs: list[float] = []
        if isinstance(rhs, Simpy):
            rhs = rhs.values
        else:
            rhs.append(rhs)
        i: int = 0
        for i in range(len(lhs)):
            if len(rhs) == 1:
                result.append(lhs[i] == rhs[0])
            else:
                result.append(lhs[i] == rhs[i])
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for >."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for values in self.values:
                result.values.append(values > rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] > rhs.values[i])
                i += 1
        return result 

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Operator overload, subscription notation."""
        result: Simpy = []
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            i: int = 0
            while i < len(rhs.values):
                if rhs[i]:
                    result.append(self.values[i])
                i += 1
        return Simpy(result)