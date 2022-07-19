#!/usr/bin/python3
"""
Module defines class Square
"""


class Square:
    """
    Defines class Square

    Args:
        size(int) - side of the square
    """

    def __init__(self, size=0):
        """
        Initialization of class Square

        Attributes:
                __size(int) - side of Square, defaults to 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
