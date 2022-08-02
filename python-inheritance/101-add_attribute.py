#!/usr/bin/python3
"""
Module 101-add_attribute.py
function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, name, value):
    """adds a new attribute  if it’s possible"""
    if ('__dict__' in dir(obj)):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
