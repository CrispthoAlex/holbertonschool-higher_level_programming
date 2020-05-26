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

Public class attribute number_of_instances: Initialized to 0

Public class attribute print_symbol: Initialized to #

def area(self): that returns the rectangle area
def perimeter(self):

if width or height is equal to 0, perimeter is equal to 0
print() and str() should print the rectangle with the character #
if width or height is equal to 0, return an empty string

repr() should return a string representation of the rectangle to be able to
 recreate a new instance by using eval()

Print the message "Bye rectangle..."
Returns the biggest rectangle based on the area
    - rect_1 must be an instance of Rectangle, otherwise raise a TypeError
    - rect_2 must be an instance of Rectangle, otherwise raise a TypeError
    - Returns rect_1 if both have the same area value
"""


class Rectangle:
    """
    initialize in constructor
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1  # number of instances created

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

    def area(self):
        """ returns the rectangle area  """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """
        prints rectangle and your representation
        """
        print_rec = ""
        anc = self.__width  # width of rectangle
        lar = self.__height  # height of rectangle
        if anc > 0 and lar > 0:
            for i in range(lar):
                print_rec += str(self.print_symbol) * anc
                print_rec += "\n"
            print_rec = print_rec[:-1]  # remove a \n
        return print_rec

    def __repr__(self):
        """  generate output for developer """
        return ('Rectangle(' + str(self.width) + ', ' + str(self.height) + ')')

    def __del__(self):
        """ An instance of Rectangle is deleted  """
        print("Bye rectangle...")
        count = Rectangle.number_of_instances
        if count > 0 and count:
            count -= 1
        Rectangle.number_of_instances = count

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
