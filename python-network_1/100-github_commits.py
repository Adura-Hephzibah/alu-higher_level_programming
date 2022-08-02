#!/usr/bin/python3
"""
Module 100-github_commits.py
"""


from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            argv[2], argv[1])
    r = requests.get(url)
    data = r.json()
    for commit in data[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
