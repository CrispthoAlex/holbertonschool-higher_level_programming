#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        revlist = reversed(my_list)
        for i in revlist:
            print("{:d}".format(i))
