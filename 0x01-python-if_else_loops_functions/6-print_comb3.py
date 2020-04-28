#!/usr/bin/python3
for i in range(9):
    for n in range(1, 10):
        if i < n:
            print("{:d}{:d}".format(i, n), end="")
            if i < 8 or n < 9:
                print(", ", end="")
            else:
                print("")
