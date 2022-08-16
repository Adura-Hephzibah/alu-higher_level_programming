#!/usr/bin/python3
"""
Module base.py
contains class Base
"""


import json


class Base:
    """Defines the class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """intialization"""
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
