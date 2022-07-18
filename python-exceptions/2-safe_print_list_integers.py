#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idex = 0
    for idex in range(x):
        try:
            print("{:d}".format(my_list[idex]), end='')
            idex += 1
        except(TypeError, ValueError):
            continue
    print()
    return idex
