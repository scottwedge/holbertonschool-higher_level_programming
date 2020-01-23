#!/usr/bin/python3
"""Unittest for base.py"""

from models.base import Base

import unittest


class TestBase(unittest.TestCase):
    """unnittest"""
    @classmethod
    def setUpClass(cls):
        """Setup for testing"""
        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base()
        cls.b4 = Base(-3)
        cls.b5 = Base(256)

    def test_class_is_type(self):
        self.assertEqual(type(self.b1), Base)

    def test_cases(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b4.id, -3)


if __name__ == "__main__":
    unittest.main()
