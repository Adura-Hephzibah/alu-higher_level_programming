#!/usr/bin/python3
"""
Module 3-say_my_name.py
function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name> <last name>
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(las_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first name} {last name}")
