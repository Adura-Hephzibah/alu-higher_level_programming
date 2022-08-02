#!/usr/bin/python3
"""
Module 0-lookup.py
contains function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """returns list of object attributes and methods"""
    return dir(obj)
