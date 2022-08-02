#!/usr/bin/python3
"""
Module 0-read_file.py

contains function that reads a text file and prints
"""


def read_file(filename=""):
    """read and print text from file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
