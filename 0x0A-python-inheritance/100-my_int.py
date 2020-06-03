#!/usr/bin/python3
""" Class Myint """


class MyInt(int):
    """
    class MyInt that inherits from int
    """

    def __eq__(self, nb):
        """
        initialitation
        """
        return True if type(nb) is self.__class__ else False

    def __ne__(self, nb):
        """
        initialitation
        """
        return True if type(nb) is not self.__class__ else False
