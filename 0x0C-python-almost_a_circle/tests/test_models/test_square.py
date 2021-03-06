#!/usr/bin/python3
"""
Unittest for square module
"""


import unittest
from models.square import Square
from models import square
import sys
import pep8
from models.base import Base
from io import StringIO


class TestSquarePep8(unittest.TestCase):
    """
    Class containing function to test Stryle of the Square class
    """
    def test_pep8(self):
        """ Testing square and test_square for pep8. """
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/square.py"
        file2 = "tests/test_models/test_square.py"
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestSquareDocs(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ Check for module documentation. """
        self.assertTrue(len(square.__doc__) > 0)


class SquareClassTests(unittest.TestCase):
    """ tests case  for class Square """

    def setUp(self):
        """
        set method class suare
        Square("size", "x", "y", "id")
        """
        self.squa0 = Square(4, 6, 2)
        self.squa1 = Square(7)
        self.squa2 = Square(2, 4)
        self.squa3 = Square(5, 9, 8, 25)
        sys.stdout = StringIO()

    def tearDown(self):
        """ After running setup clear everything """
        sys.stdout = sys.__stdout__

    def test_sq0(self):
        """Normal Cases"""
        squa_1 = Square(6)
        self.assertEqual(squa_1.size, 6)
        squa_2 = Square(8, 3, 2)
        self.assertEqual(squa_2.size, 8)
        self.assertEqual(squa_2.x, 3)
        self.assertEqual(squa_2.y, 2)

    def test_typeError(self):
        """ test typeError from square's attributes """
        self.assertRaises(TypeError, Square, "a", 2, 7)
        self.assertRaises(TypeError, Square, 2, "3", 9)
        self.assertRaises(TypeError, Square, 6, 3, "9")
        self.assertRaises(TypeError, Square, [1, 2], 7, 8)
        self.assertRaises(TypeError, Square, 2, 3.5, 9)
        self.assertRaises(TypeError, Square, 2, 5, {1, 2})
        self.assertRaises(TypeError, Square, 8, (1, 2), 9.5)
        self.assertRaises(TypeError, Square, None, 8, 9)
        self.assertRaises(TypeError, Square, 197, 5j, 19)
        self.assertRaises(TypeError, Square, 10, 2, float("inf"))
        self.assertRaises(TypeError, Square, 222, "crispthofer", 980)
        self.assertRaises(TypeError, Square)

    def test_valueError(self):
        """ test square value error  """
        self.assertRaises(ValueError, Square, -8, 7, 8)
        self.assertRaises(ValueError, Square, 2, -5, 9)
        self.assertRaises(ValueError, Square, 2, 5, -10)

    def test_areaSq(self):
        """ test square area """
        self.assertEqual(self.squa0.area(), 16)
        self.assertEqual(self.squa1.area(), 49)
        self.assertEqual(self.squa2.area(), 4)
        self.assertEqual(self.squa3.area(), 25)

    def test_display_square(self):
        """
        test stdout the Square instance
        Square(4, 6, 2)
        """

        squa_disp = "\n"\
                    "\n"\
                    "      ####\n"\
                    "      ####\n"\
                    "      ####\n"\
                    "      ####\n"

        self.squa0.display()
        self.assertEqual(sys.stdout.getvalue(), squa_disp)

    def test_str_module(self):
        """
        squa0(4, 6, 2) - squa1(7)
        squa2(2, 4) - squa3(5, 9, 8, 25)
        """
        squa0 = Square(4, 6, 2, 12)
        squa1 = Square(7, 0, 0, 13)
        squa2 = Square(2, 4, 0, 14)
        squa3 = Square(5, 9, 8, 25)
        self.assertEqual(squa0.__str__(),
                         "[Square] (12) 6/2 - 4")
        self.assertEqual(squa1.__str__(),
                         "[Square] (13) 0/0 - 7")
        self.assertEqual(squa2.__str__(),
                         "[Square] (14) 4/0 - 2")
        self.assertEqual(squa3.__str__(),
                         "[Square] (25) 9/8 - 5")

    def test_update(self):
        """
        tests update module for square. args || kwargs
        ["id", "size", "x", "y"]
        """
        self.squa0.update(10, 9)
        self.assertEqual(self.squa0.__str__(), "[Square] (10) 6/2 - 9")
        self.squa3.update(x=5, y=7, size=8, id=7)
        self.assertEqual(self.squa3.__str__(), "[Square] (7) 5/7 - 8")

    def test_squa_dict(self):
        """ test represent dictionary """
        dic0 = Square(10, 6, 2, 1).to_dictionary()
        dic_temp = {'size': 10, 'x': 6, 'id': 1, 'y': 2}
        self.assertEqual(dic0, dic_temp)
        self.assertEqual(dic0 is dic_temp, False)

if __name__ == '__main__':
    unittest.main()
