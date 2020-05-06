#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or tuple_a == ():
        tuple_a += (0, 0)
    if len(tuple_b) < 2 or tuple_b == ():
        tuple_b += (0, 0)
    if tuple_a != () and tuple_b != ():
        return(tuple(sum(i) for i in zip(tuple_a, tuple_b)))

#  zip() https://realpython.com/python-zip-function/
#  /understanding-the-python-zip-function
