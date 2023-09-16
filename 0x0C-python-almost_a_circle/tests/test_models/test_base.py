#!/usr/bin/python3
"""Usitest for the Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Base Class """

    def test_instace_creation_with_id(self):
        """ Test instance creation with id """
        b = Base(41)
        self.assertEqual(b.id, 41)

    def test_instance_creation_without_id(self):
        """ Test instance creation without id """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)


if __name__ == "__main__":
    unittest.main()
