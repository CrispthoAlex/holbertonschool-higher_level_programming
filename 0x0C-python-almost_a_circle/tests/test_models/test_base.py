#!/usr/bin/python3
"""
Onittest class Base
"""


import unittest
from models.base import Base


class BaseclassTests(unittest.TestCase):
    """ Test cases """

    def setup(self):
        """ count instances """
        Base._Base__nb_objects = 0

    def test_n(self):
        """ id = None && id = n  """
        base_0 = Base()
        base_1 = Base(12)
        base_2 = Base()

        self.assertEqual(base_0.id, 1)
        self.assertEqual(base_1.id, 12)
        self.assertEqual(base_2.id, 2)

    def test_txt(self):
        """ Enter id = "txt"  """
        base_0 = Base("holbie")
        self.assertEqual(base_0.id, "holbie")

if __name__ == '__main__':
    unittest.main()
