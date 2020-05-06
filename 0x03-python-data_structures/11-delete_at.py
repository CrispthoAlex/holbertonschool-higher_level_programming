#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        newlist = my_list
        del newlist[idx]  # del removes the item at a specific index
        return(newlist)
    return(my_list)
