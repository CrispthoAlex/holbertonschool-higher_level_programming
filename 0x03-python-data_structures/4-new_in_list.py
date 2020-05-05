#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list and (idx >= 0 and idx < len(my_list)):
        newlist = my_list.copy()
        newlist[idx] = element
        return(newlist)
    return(my_list)
