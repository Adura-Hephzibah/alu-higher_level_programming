#!/usr/bin/python3
"""
Module 2-matrix_divided.py
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix

    Args:
        matrix -  must be a list of lists of integers or floats
        div must be a number (integer or float)

    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    msg_1 = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list):
        raise TypeError(msg)
    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
        if len(row) != len(matrix[0]):
            raise TypeError(msg_1)

    new = [[round((i/div), 2) for i in row] for row in matrix]
    return new
