#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        newlist = my_list
        newlist[idx] = element
        return(newlist)
    return(my_list)
