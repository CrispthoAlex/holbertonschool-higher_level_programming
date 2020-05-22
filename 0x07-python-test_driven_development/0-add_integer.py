#!/usr/bin/python3
"""
Return addition of a and b

>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """Return the factorial of n, an exact integer >= 0. Addition module

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
