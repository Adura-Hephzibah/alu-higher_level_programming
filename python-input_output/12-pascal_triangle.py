#!/usr/bin/python3
"""
Module 12-pascal_triangle.py

function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    tri = [[1]]
    for row in range(n-1):
        tri.append([i+j for i, j in
                   zip([0]+tri[-1], tri[-1] + [0])])
    return tri
