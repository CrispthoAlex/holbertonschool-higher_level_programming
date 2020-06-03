#!/usr/bin/python3
"""
adds a new attribute to an object if its possible
"""


def add_attribute(obje, uname, value):
    """set attrib
    Args:
    @obje: Object
    @uname: name
    @value: instance
    """
    if obje.__class__.__module__ == 'builtins':
        raise TypeError("can't add new attribute")
    setattr(obje, uname, value)
