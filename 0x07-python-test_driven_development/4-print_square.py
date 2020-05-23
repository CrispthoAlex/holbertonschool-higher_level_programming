#!/usr/bin/python3
"""
Prints  a square with the character #
>>> print_square()
My name is Crispthofer Rincon
"""


def print_square(size):
    """Prints My name is <first name> <last name>

    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
