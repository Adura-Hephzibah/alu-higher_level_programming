#!/usr/bin/python3
"""
locked class that prevents dynamically creating
instance attributes
"""


class LockedClass:
    """prevent dynamically created attributes"""
    __slots__ = "first_name"
