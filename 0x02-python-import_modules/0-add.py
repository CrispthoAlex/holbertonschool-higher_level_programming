#!/usr/bin/python3
from add_0 import add
a = 1
b = 2
if __name__ == "__main__":
    if a != int(a) or b != int(b):
        print("")
    else:
        print("{:d} + {:d} = {:d}".format(a, b, add(a + b)))
