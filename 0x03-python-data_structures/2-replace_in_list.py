#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx > 0 and idx < len(my_list):
        newlist = my_list.copy()
        newlist[idx] = element
        return(newlist)
    else:
        return(my_list)
