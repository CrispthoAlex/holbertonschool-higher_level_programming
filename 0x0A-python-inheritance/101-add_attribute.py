#!/usr/bin/python3
""" adds a new attribute to an object if its possible """


def add_attribute(obje, key, value):
    """set attrib
    Args:
        @obje: Object
        @key: key
        @value: valuee
    * hsattr: The arguments are an object and a string.
      The result is True if the string is the name of one
      of the objects attributes, False if not
    """
    if hasattr(obje, "__dict__"):
        setattr(obje, key, value)
    else:
        raise TypeError("can't add new attribute")
