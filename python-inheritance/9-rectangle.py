#!/usr/bin/python3
"""
Module 9-rectangle.py
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from class BaseGeometry"""

    def __init__(self, width, height):
        """initialization"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """implements area method and return area"""
        return self.__width * self.__height

    def __str__(self):
        """returns [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(type(self).__name__,
                                         self.__width, self.__height)
