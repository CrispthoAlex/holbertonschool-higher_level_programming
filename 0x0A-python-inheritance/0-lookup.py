#!/usr/bin/python3
"""
Lookup: Write a function that returns the list of available attributes and
methods of an object
"""


def lookup(obj):
    """
    Args: obj
    Returns a list object
    """
    return dir(obj)
