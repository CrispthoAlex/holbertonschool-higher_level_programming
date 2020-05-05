#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    newlist = my_list
    if idx > 0 and idx < len(my_list):
        newlist[idx] = element
    return(newlist)
