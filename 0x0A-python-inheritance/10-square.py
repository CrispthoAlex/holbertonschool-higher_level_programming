#!/usr/bin/python3
""" Class Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        """
        * Instantiation size:
            Validated by integer_validator
        Args: @size: size
        """
        super().integer_validator("size", size)  # validator of class Rectangle
        self.__size = size
        super().__init__(self.__size, self.__size)  # init width and height

    def area(self):
        """
        Area method
        Args: @self: size
        """
        return self.__size ** 2
