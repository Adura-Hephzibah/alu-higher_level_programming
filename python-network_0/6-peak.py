#!/usr/bin/python3
"""
Module 6-peak.py
"""


def find_peak(list_of_integers):
    """returns peak"""
    list_of_integers.sort()
    return list_of_integers[-1]
