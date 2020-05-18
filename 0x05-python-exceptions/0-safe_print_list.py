#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nprint = 0  # numbers of elements printed
    for item in range(x):
        try:
            print(my_list[item], end='')
            nprint += 1
        except:
            break
    print()
    return (nprint)
