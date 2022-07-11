#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str) or roman_string is None:
        return 0
    if type(roman_string) is str:
        nar = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        add = 0
        for x, y in zip(roman_string, roman_string[1:]):
            if x not in nar.keys():
                return 0
            elif nar[x] >= nar[y]:
                add += nar[x]
            else:
                add -= nar[x]
        add += nar[roman_string[-1]]
        return add
