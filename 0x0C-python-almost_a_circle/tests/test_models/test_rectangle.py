#!/usr/bin/python3
"""Unittest for base.py"""

from models.base import Base
from models.rectangle import Rectangle

import unittest


class TestRectangle(unittest.TestCase):
    """unnittest"""

    def SetUp(self):
        Base.Base__nb_objects = 0

    def test_type(self):
        r1 = Rectangle(4, 8)
        self.assertTrue(type(r1), Rectangle)


if __name__ == "__main__":
    unittest.main()
