#!/usr/bin/python3
"""
Module 9-student.py

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

    def to_json(self):
        """Public method to retrieve dictionary representation"""

        return self.__dict__
