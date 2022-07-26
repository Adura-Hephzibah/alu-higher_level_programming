#!/usr/bin/python3
"""
Module 2-is_same_class.py
contains function that returns True if the object is
exactly an instance
"""


def is_same_class(obj, a_class):
    """return True if obj is exactly an instance"""
    return isinstance(obj, a_class)
