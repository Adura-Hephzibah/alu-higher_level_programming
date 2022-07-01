#!/usr/bin/python3
def uppercase(str):
    upp = ''
    for i in str:
        if (i >= 'a' and i <= 'z'):
            upp = upp + chr((ord(i) - 32))
        else:
            upp = upp + i
    print("{}".format(upp))
