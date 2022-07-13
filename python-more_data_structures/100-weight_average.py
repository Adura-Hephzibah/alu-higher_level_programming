#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        sums = 0
        dvd = 0
        for tup in my_list:
            scores, weight = tup
            sums += scores * weight
            dvd += weight
        return (sums / dvd) if dvd > 0 else 0
    else:
        return 0
