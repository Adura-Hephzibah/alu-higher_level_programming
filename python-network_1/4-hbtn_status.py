#!/usr/bin/python3
"""
Module 4-hbtn_status.py
fetches https://intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
