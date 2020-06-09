#!/usr/bin/python3
"""
Unittest class Base
"""


import unittest
import pep8
import json
import sys
from models import base
from models.base import Base


class TestPep8B(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base.py'
        file2 = 'tests/test_models/test_base.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)


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

    def test_to_json(self):
        """ to json string """
        a = Base.to_json_string(None)
        self.assertEqual(a, "[]")


if __name__ == '__main__':
    unittest.main()
