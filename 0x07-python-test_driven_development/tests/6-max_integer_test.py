#!/usr/bin/python3
""" Unittests for max_integer([]). """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unitteses for max_integer([]). """

    def test_empty_list(self):
        """ Test an empty list """
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """ test list of one element """
        self.assertEqual(max_integer([7]), 7)

    def test_ordered_list(self):
        """ Test an ordered list """
        self.assertEqual(max_integer([0, 1, 5, 7]), 7)

    def test_unordered_list(self):
        """ Test an unorderd list """
        self.assertEqual(max_integer([5, 3, 2]), 5)

    def test_negative_numbers(self):
        """ test negative numbers """
        self.assertEqual(max_integer([-5, -4, -2]), -2)

    def test_mixed_numbers(self):
        """ tes mixed numbers """
        self.assertEqual(max_integer([5, -8, -4, 10]), 10)

    def test_float(self):
        """ test float """
        self.assertEqual(max_integer([2.14, -4.1, 8, 0, 10]), 10)

    def test_string(self):
        """ test string """
        self.assertEqual(max_integer("amine"), 'n')

    def test_list_of_strings(self):
        """ test a list of strings """
        self.assertEqual(max_integer(["test", "amine", "bron"]), "test")





if __name__ == '__main__':
    unittest.main()
