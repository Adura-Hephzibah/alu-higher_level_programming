#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[x**2 for x in row]for row in matrix]

# alternative:
# return(list(map(lambda x: x**2, row)) for row in matrix)
