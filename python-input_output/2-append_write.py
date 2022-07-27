#!/usr/bin/python3
"""
Module 2-append_write.py

function appends a string to text file, returns number of char
"""


def append_file(filename="", text=""):
    """writes a string to text file, returns number of char"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
