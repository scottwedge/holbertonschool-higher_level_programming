#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Write a class Square that defines a square by: (based on 1-square.py)"""

    def __init__(self, size=0):
        """Inizialitation

        Args:
            size (int): Private instance attribute: size.
        """
        self.size = size

    @property
    def size(self):
        """Get and Set"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set value
        Args:
            value (int): size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ return the area

        Returns:
            the return value is the area
        """
        return self.__size**2

    def my_print(self):
        """that prints in stdout the square with the character #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
