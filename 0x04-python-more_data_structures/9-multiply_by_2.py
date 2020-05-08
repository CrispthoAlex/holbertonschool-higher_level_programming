#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        new_dic = a_dictionary.copy()
        for k, v in new_dic.items():  # value*2
            new_dic[k] = v * 2
        return (new_dic)
    return (a_dictionary)
