#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lnum = ((-1 * number) % 10)
    else:
        lnum = number % 10
    print("{:d}".format(lnum), end="")
    return (lnum)
