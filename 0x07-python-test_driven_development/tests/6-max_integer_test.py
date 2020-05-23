#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        interactive tests for max integer module

    """
    def test_max_integer(self):
        """ Find maximun integer in a list
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-10, -2, -103]), -2)
        self.assertEqual(max_integer([-1.5, -5.2, 10.3]), 10.3)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([45, 45, 45, 45]), 45)
        self.assertEqual(max_integer([5.6, 34, 5, 45.8]), 45.8)
        self.assertEqual(max_integer([80]), 80)
