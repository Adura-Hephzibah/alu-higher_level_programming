#!/usr/bin/python3
"""
Module 7-base_geometry.py
contains class BaseGeometry
"""


class BaseGeometry:
    """defines class BaseGeometry"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
