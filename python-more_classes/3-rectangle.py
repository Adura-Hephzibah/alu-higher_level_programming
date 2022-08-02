#!/usr/bin/python3
"""
Module 3-rectangle.py
allows printing rectangle with #
using print() or str()
"""


class Rectangle:
    """
    Defines class Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialization
        Attributes: width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """print the rectangle with the character #"""
        str_t = ""
        if self.__width == 0 or self.__height == 0:
            return str_t
        else:
            str_t += "\n".join("#"*self.__width for _ in range(self.__height))
            return str_t
