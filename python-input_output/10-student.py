#!/usr/bin/python3
"""
Module 10-student.py

Defines class Student with public instance attributes
of first_name, last_name, age
"""


class Student:
    """Class Definition"""

    def __init__(self, first_name, last_name, age):
        """Initializes student with names and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method"""

        if attrs is None:
            return self.__dict__
        else:
            nary = {}
            for item in attrs:
                if item in self.__dict__.keys():
                    nary[item] = self.__dict__[item]
            return nary
