#!/usr/bin/python3
"""
Prints a string with first_name and last_name
>>> say_my_name("Crispthofer", "Rincon")
My name is Crispthofer Rincon
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
