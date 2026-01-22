#!/usr/bin/python3
"""
Module that defines a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers.

    a and b must be integers or floats.
    Floats are casted to integers before addition.

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
