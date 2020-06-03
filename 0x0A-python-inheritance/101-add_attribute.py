#!/usr/bin/python3
""" adds a new attribute to an object if its possible """


def add_attribute(obje, key, value):
    """set attrib
    Args:
        @obje: Object
        @key: key
        @value: valuee
    """
    if hasattr(obje, "__dict__"):
        setattr(obje, key, value)
    else:
        raise TypeError("can't add new attribute")
