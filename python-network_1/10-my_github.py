#!/usr/bin/python3
"""
Module 10-my_github.py
"""


import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    dic = r.json()
    print(dic["id"])
