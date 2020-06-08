#!/usr/bin/python3
""" Class Rectangle inherits from Base  """


from models.base import Base


class Rectangle(Base):
    """ class Rectangle that defines a rectangle  """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """  getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """  getter """
        return self.__height

    @height.setter
    def height(self, value):
        """  setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area value of the Rectangle instance  """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #
        """
        for y in range(self.__y):
            print()
        for n in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """  returns [Rectangle] (id) x/y - width/height """
        a = self.id
        b = self.__x
        c = self.__y
        d = self.__width
        e = self.__height
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(a, b, c, d, e)

    def update(self, *args, **keywords):
        """
        assigns an argument to each attribute:
        1st argument - id attribute, 2nd argument - width attribute
        3rd argument - height attribute, 4th argument - x attribute
        5th argument - y attribute
        """
        if args and len(args) > 0:
            attri_list = ["id", "width", "height", "x", "y"]
            for item, value in enumerate(args):
                if item < 5:
                    setattr(self, attri_list[item], value)
        else:  # become to dictionary
            for key, value in keywords.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ public method that returns the dictionary representation """
        attri_dic = ["id", "width", "height", "x", "y"]
        dic_rec = {}
        for key in attri_dic:
            dic_rec.update({key: getattr(self, key)})
        return dic_rec
        # {key: getattr(self, key) for key in attri_dic}
