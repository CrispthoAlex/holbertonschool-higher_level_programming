#!/usr/bin/python3
""" Class Square inherits from Base  """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that defines a square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initiation """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ represent a square
        [Square] (<id>) <x>/<y> - <size>
        """
        a = self.id
        b = self.x
        c = self.y
        d = self.size
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(a, b, c, d)

    @property
    def size(self):
        """ getter attribute for size """
        return self.width

    @size.setter
    def size(self, side):
        """ setter size """
        self.width = side
        self.height = side

    def update(self, *args, **keywords):
        """
        assigns an argument to each attribute:
        1st argument - id attribute, 2nd argument - size attribute
        3rd argument - x attribute, 4th argument - y attribute
        """
        if args and len(args) > 0:
            attri_list = ["id", "size", "x", "y"]
            for item, value in enumerate(args):
                if item < 4:
                    setattr(self, attri_list[item], value)
        else:  # become to dictionary
            for key, value in keywords.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ public method that returns the dictionary representation """
        attri_dic = ["id", "size", "x", "y"]
        dic_squa = {}
        for key in attri_dic:
            dic_squa.update({key: getattr(self, key)})
        return dic_squa
        # {key: getattr(self, key) for key in attri_dic}
