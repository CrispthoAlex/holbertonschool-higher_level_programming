#!/usr/bin/python3
"""
returns True if the object is exactly an instance of the
specified class ; otherwise False.

"""


def is_same_class(obj, a_class):
    """
    Args: @obj: object
          @a_class: class
    """
    return True if type(obj) == a_class else False
