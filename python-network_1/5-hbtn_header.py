#!/usr/bin/python3
"""
Module 5-hbtn_header.py
"""


from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    ptr = r.headers.get('X-Request-Id')
    print(ptr)
