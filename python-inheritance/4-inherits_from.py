#!/usr/bin/python3
"""
Module 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    True if obj is instance of class that inherits
    (directly or indirectly) from the specified class
    """
    return issubclass(type(obj), a_class)
