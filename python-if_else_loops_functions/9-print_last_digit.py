#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        dgt = number % (-10)
    else:
        dgt = number % 10
    return dgt
