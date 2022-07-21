#!/usr/bin/python3
"""This Module defines class MagicClass"""
import math


class MagicClass:
    """
    Defines class MagicClass with atrributes and methods
    """
    def __init__(self, radius=0):
        """Initializes MagicClass"""
        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculates area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calculates circumference"""
        return 2 * math.pi * self.__radius
