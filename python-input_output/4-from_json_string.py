#!/usr/bin/python3
"""
Module 4-from_json_string.py

function that returns an object (Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """returns python data structure frm JSON"""
    import json

    return json.loads(my_str)
