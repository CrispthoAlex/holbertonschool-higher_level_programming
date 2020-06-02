#!/usr/bin/python3
"""
class MyList from list:

def print_sorted(self): that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    Args: list from main
    """

    def print_sorted(self):
        """
        Public instance method that prints the list, but
        sorted (ascending sort)
        Args: @self: inherits the input from self
        """
        print(sorted(self))
