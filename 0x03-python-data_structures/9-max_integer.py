#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        lsort = sorted(my_list)
        return(lsort[-1])
    return (None)

#  return(tuple(sum(i) for i in zip(tuple_a, tuple_b))) <-- remember

#  zip() https://realpython.com/python-zip-function/
#  /understanding-the-python-zip-function
