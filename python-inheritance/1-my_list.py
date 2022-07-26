#!/usr/bin/python3
"""
Module 1-my_list.py
contains class MyList
inherits from list and has public instance method
"""


class MyList(list):
    """
    defines class MyList
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
