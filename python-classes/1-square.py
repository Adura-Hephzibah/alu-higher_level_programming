#!/usr/bin/python3
"""
This Module - 1-square.py
defines a class Square with private instance attribute
"""


class Square:
    """
    class Square definition

    Args:
         size - side of square
    """
    def __init__(self, size):
        """
        Initializes square

        Attributes:
            size - side of a square
        """
        self.__size = size
