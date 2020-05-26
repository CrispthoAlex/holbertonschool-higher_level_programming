#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
def __init__(self, width=0, height=0):
def width(self)
width must be an integer, otherwise raise a TypeError
width is less than 0, raise a ValueError
def height(self)
height must be an integer, otherwise raise a TypeError
height is less than 0, raise a ValueError
"""


class Rectangle:
    """
    initialize in constructor
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """  getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """  getter """
        return self.__height

    @height.setter
    def height(self, value):
        """  setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
