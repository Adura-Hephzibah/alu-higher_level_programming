#!/usr/bin/python3
"""
Module 1-hbtn_header.py
takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""


import urllib.request
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        data = response.getheader('X-Request-Id')
        print(data)
