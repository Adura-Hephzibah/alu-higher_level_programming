#!/usr/bin/python3
"""
Module 3-square
defines class Square
"""


class Square:
    """
    definition of class Square

    Args:
        size
    """

    def __init__(self, size=0):
        """
        Initialization

        Attributes: __size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ calculates the area"""

        return (self.__size) ** 2
