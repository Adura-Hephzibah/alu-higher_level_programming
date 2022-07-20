#!/usr/bin/python3
"""
Module 4-square.py
defines class Square
"""


class Square:
    """class Square definition

    Args: size(int) - side of the square
    """

    def __init__(self, size=0):
        """
                Initialization of square
                Attributes: Size(int) - defaults to zero if no value
        """
        self.size = size


    @property
    def size(self):
        """getter"""
        return self.__size


    @size.setter
    def size(self, value):
        """ setter

            sets size to value if value is int and greater than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates area of the square"""
        return (self.__size)**2
