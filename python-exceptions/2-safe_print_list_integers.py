#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idex = 0
    while idex < x:
        try:
            print("{:d}".format(my_list[idex]), end='')
        except(TypeError, ValueError):
            continue
        idex += 1
    print()
    return idex
