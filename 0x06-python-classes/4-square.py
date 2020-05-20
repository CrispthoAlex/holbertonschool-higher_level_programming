#!/usr/bin/python3
"""
Size validation mandatory: Write a class Square that defines a square by:
(based on 1-square.py)

* Private instance attribute: size
  - property def size(self): to retrieve it
  - property setter def size(self, value): to set it:
    + size must be an integer, otherwise raise a TypeError exception with the
 message size must be an integer
    + if size is less than 0, raise a ValueError exception with the message
 size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):

* Public instance method: def area(self): that returns the current square area

* You are not allowed to import any module
"""


class Square:
    """ init __size and area() method """
    __size = 0

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area method """
        squasize = self.__size
        return (squasize ** 2)

    @property
    def size(self):
        """ getter size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
