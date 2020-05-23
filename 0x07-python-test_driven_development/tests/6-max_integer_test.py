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

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def setUp(self):
        pass

    def test_all_same(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_ordered_list(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        unordered = [2, 3, 4, 1]
        self.assertEqual(max_integer(unordered), 4)

    def test_single_element_list(self):
        single_element_list = [18]
        self.assertEqual(max_integer(single_element_list), 18)

    def test_negatives(self):
        test_list = [-4, 0, 6, 4]
        self.assertEqual(max_integer(test_list), 6)

        test_list = [-7, -6, -5, -4]
        self.assertEqual(max_integer(test_list), -4)

    def test_max_integer(self):
        test_list = [1, 2, 3, 9, 4]
        self.assertEqual(max_integer(test_list), 9)

    def test_max_integer_neg(self):
        test_list = [1, 2, 3, 4, 5, -10, -100, -1000, 0]
        self.assertEqual(max_integer(test_list), 5)

    def test_max_integer_(self):
        self.assertEqual(max_integer([]), None)

    def test_positives(self):
        test_list = [4, 2, 3, 1]
        self.assertEqual(max_integer(test_list), 4)
