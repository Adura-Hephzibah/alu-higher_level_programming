#!/usr/bin/python3
"""
Module 8-json_api.py
"""


import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    dic = {"q": letter}
    r = requests.post('http://0.0.0.0:5000/search_user', data=dic)
    dic_1 = r.json()
    try:
        if dic_1:
            print("[{}] {}".format(dic_1.get('id'), dic_1.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
