#!/usr/bin/python3
"""
Unittest for rectangle module
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models import rectangle
import sys
import pep8
from io import StringIO


class TestRectanglePep8(unittest.TestCase):
    """ checking for pep8 validation """
    def test_pep8(self):
        """ test rectangle and test_rectangle
            for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/rectangle.py'
        file2 = 'tests/test_models/test_rectangle.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestRecDocs(unittest.TestCase):
    """ checking for documentation """
    def test_module_doc(self):
        """ checking for module documentation """
        self.assertTrue(len(rectangle.__doc__) > 0)

    def test_class_doc(self):
        """ checking for class documentation """
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_method_docs(self):
        """ checking for method documentation """
        for func in dir(Rectangle):
            self.assertTrue(len(func.__doc__) > 0)


class RectangleClassTests(unittest.TestCase):
    """ tests case  """

    def setUp(self):
        """ set method  """
        Base._Base__nb_objects = 0
        self.rec0 = Rectangle(4, 6, 2, 2)
        self.rectangle_1 = Rectangle(1, 7)
        self.rectangle_2 = Rectangle(2, 4, 0, 3)
        self.rectangle_3 = Rectangle(2, 5)
        sys.stdout = StringIO()

    def tearDown(self):
        """ After running setup clear everything """
        sys.stdout = sys.__stdout__

    def test_r0(self):
        """Normal Cases"""
        rec_1 = Rectangle(2, 6)
        self.assertEqual(rec_1.width, 2)
        self.assertEqual(rec_1.height, 6)
        rec_2 = Rectangle(8, 3, 1, 2)
        self.assertEqual(rec_2.width, 8)
        self.assertEqual(rec_2.height, 3)
        self.assertEqual(rec_2.x, 1)
        self.assertEqual(rec_2.y, 2)

    def test_r1(self):
        """ TypeError case  """
        self.assertRaises(TypeError, Rectangle, "a", 2, 7, 8)
        self.assertRaises(TypeError, Rectangle, 2, 3, "3", 9)
        self.assertRaises(TypeError, Rectangle, 2, "3", 5, 9)
        self.assertRaises(TypeError, Rectangle, 8, 6, 3, "9")

    def test_r2(self):
        """ TypeError case  """
        self.assertRaises(TypeError, Rectangle, [1, 2], 2, 7, 8)
        self.assertRaises(TypeError, Rectangle, 2, 3, 3.5, 9)
        self.assertRaises(TypeError, Rectangle, 2, {1, 2}, 5, 9)
        self.assertRaises(TypeError, Rectangle, 8, 6, 3, (1, 2))

    def test_r3(self):
        """ TypeError case  """
        self.assertRaises(ValueError, Rectangle, -8, 2, 7, 8)
        self.assertRaises(ValueError, Rectangle, 2, 3, -5, 9)
        self.assertRaises(ValueError, Rectangle, 2, -8, 5, 9)
        self.assertRaises(ValueError, Rectangle, 8, 6, 3, -5)

    def test_r4(self):
        """ TypeError case  """
        self.assertRaises(TypeError, Rectangle, None, 3, 6, 8, 9)
        self.assertRaises(TypeError, Rectangle, 222, 197, 5j, 19)
        self.assertRaises(TypeError, Rectangle, 2, float("inf"), 8, 1)
        self.assertRaises(TypeError, Rectangle, 222, 197, "crispthofer", 2398)
        self.assertRaises(TypeError, Rectangle)

    def test_area(self):
        """ TypeError case  """
        self.assertEqual(self.rec0.area(), 24)
        self.assertEqual(self.rectangle_1.area(), 7)
        self.assertEqual(self.rectangle_2.area(), 8)
        self.assertEqual(self.rectangle_3.area(), 10)

    def test_display_5_7(self):  # Rectangle(4, 6, 2, 2)
        """ test stdout the Rectangle instance  """

        recta_disp = "\n"\
                     "\n"\
                     "  ####\n"\
                     "  ####\n"\
                     "  ####\n"\
                     "  ####\n"\
                     "  ####\n"\
                     "  ####\n"
        self.rec0.display()
        self.assertEqual(sys.stdout.getvalue(), recta_disp)

    def test_str(self):
        """ test stdout the Rectangle instance """
        rec_t0 = Rectangle(4, 6, 2, 2, 1)
        rec_t1 = Rectangle(1, 7, 0, 0, 1)
        rec_t2 = Rectangle(2, 4, 0, 3, 1)
        rec_t3 = Rectangle(2, 5, 0, 0, 1)
        self.assertEqual(rec_t0.__str__(),
                         "[Rectangle] (1) 2/2 - 4/6")
        self.assertEqual(rec_t1.__str__(),
                         "[Rectangle] (1) 0/0 - 1/7")
        self.assertEqual(rec_t2.__str__(),
                         "[Rectangle] (1) 0/3 - 2/4")
        self.assertEqual(rec_t3.__str__(),
                         "[Rectangle] (1) 0/0 - 2/5")

    def test_update_t8(self):
        """ test for assigns a key/value argument to attributes, with *args
        [Rectangle] (id) x/y - width/height
        Rectangle(4, 6, 2, 2)
        """
        self.rec0.update(15, 4, 9, 3, 2)
        self.assertEqual(self.rec0.__str__(), "[Rectangle] (15) 3/2 - 4/9")

    def test_update_t9(self):
        """ test for assigns a key/value argument to attributes, with **kwargs
        [Rectangle] (id) x/y - width/height
        Rectangle(4, 6, 2, 2)
        """
        self.rec0.update(width=4, height=9, id=1)
        self.assertEqual(self.rec0.__str__(), "[Rectangle] (1) 2/2 - 4/9")
        self.rec0.update(x=10, id=15, height=9)
        self.assertEqual(self.rec0.__str__(), "[Rectangle] (15) 10/2 - 4/9")

    def test_rec_dict(self):
        """ test represent dictionary """
        dic0 = Rectangle(4, 6, 2, 2, 1).to_dictionary()
        dic_temp = {'height': 6, 'x': 2, 'id': 1, 'y': 2, 'width': 4}
        self.assertEqual(dic0, dic_temp)
        self.assertEqual(dic0 is dic_temp, False)


if __name__ == '__main__':
    unittest.main()
