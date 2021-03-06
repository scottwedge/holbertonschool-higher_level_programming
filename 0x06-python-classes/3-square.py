#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Write a class Square that defines a square by: (based on 1-square.py)"""

    def __init__(self, size=0):
        """Inizialitation

        Args:
            size (int): Private instance attribute: size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the area

        Returns:
            the return value is the area
        """
        return self.__size**2
