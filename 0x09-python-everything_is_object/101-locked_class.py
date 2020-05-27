#!/usr/bin/python3
"""
Low memory cost: class LockedClass with no class or object attribute, that
 prevents the user from dynamically creating new instance attributes, except
if the new instance attribute is called first_name
"""


class LockedClass():
    """
    prevents the user from dynamically creating new instance attributes, except
    attribute is called first_name
    """
    __slots__ = ['first_name']
