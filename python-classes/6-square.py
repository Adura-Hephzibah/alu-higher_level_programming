#!/usr/bin/python3
"""
Module 6-square.py
defines class Square
"""


class Square:
    """class Square definition

    Args: size(int) - side of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
                Initialization of square
                Attributes: Size(int) - defaults to zero if no value
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter"""
        if type(value) != tuple or len(value) != 2 or \
           type(value[0]) != int or type(value[1]) != int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates area of the square"""
        return (self.__size)**2

    def my_print(self):
        """draw square using # symbol depending on value of __size"""
        if self.__size != 0:
            for j in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
