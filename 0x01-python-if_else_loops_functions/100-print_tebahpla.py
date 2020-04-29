#!/usr/bin/python3
for i in reversed('abcdefghijklmnopqrstuvwxyz'):
    if ord(i) % 2 == 1:
        print("{:s}".format(str.upper(i)), end="")
    else:
        print("{:s}".format(i), end="")
