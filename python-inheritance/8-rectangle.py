#!/usr/bin/python3
"""
Module 8-rectangle.py
"""


from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from class BaseGeometry"""
    def __init__(self, width, height):
        """initialization"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
