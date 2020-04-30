#!/usr/bin/python3
import sys
if __name__ == "__main__":
    nuargv = len(sys.argv) - 1  # number of arguments
    colon = ':.'
    if nuargv > 0:
        if nuargv == 1:
            print("{:d} argument:".format(nuargv))
        else:
            print("{:d} arguments{:s}".format(nuargv, colon[0]))
        for i in range(1, nuargv + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
    if nuargv == 0:
        print("{:d} arguments{:s}".format(nuargv, colon[1]))
