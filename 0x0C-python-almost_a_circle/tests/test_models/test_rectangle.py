#!/usr/bin/python3
"""Unittest for base.py"""

from models.base import Base
from models.rectangle import Rectangle

import unittest


class TestRectangle(unittest.TestCase):
    """unittest"""

    def SetUp(self):
        Base.Base__nb_objects = 0

    def test_A_constructor(self):
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
            error = 'test'
            print(str(e.exception))
        self.assertEqual(str(e.exception), error)


if __name__ == "__main__":
    unittest.main()
