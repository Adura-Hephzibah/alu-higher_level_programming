#!/usr/bin/python3
"""
Module 0-add_integer.py
function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds two numbrs and returns the result.
    Arguments are casted into integer if any is a float

    Args:
        a : first number which can be int or float
        b : second number which can be int or float

    Returns: Sum of the two numbers

    Raises: TypeError if a or b is not int or float

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
