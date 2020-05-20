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

* Square instance can answer to comparators: ==, !=, >, >=, < and <= based
  on the square area

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

    def area(self):
        """ area method """
        return (self.__size ** 2)

    def __eq__(self, other):
        """Equal == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not Equal != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less equal <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """great than > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """great equal >= compmarison to a Square."""
        return self.area() >= other.area()
