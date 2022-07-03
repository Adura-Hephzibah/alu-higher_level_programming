#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    entry = argv[1:]
    size = len(entry)
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if size != 1 else "argument",
                 "." if size == 0 else ":"))
    for count, arg in enumerate(entry, 1):
        print("{:d}: {:s}".format(count, arg))
