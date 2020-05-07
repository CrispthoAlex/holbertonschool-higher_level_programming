#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        addlist = set(my_list)
        i = 0
        for item in addlist:
            i += item
        return (i)
    return (0)
