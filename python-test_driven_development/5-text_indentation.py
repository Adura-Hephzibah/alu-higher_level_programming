#!/usr/bin/python3
"""
Module 5-text_indentation.py
function that prints a text with 2 new lines after each of
these characters: ".", "?" and ":"
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    new = text.split('\n')
    for line in new:
        item = line.strip(' ')
        print(item)
