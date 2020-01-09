#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Write a class Square that defines a square by: (based on 1-square.py)"""

    def __init__(self, size=0, position=(0, 0)):
        """Inizialitation

        Args:
            size (int): Private instance attribute: size.
            position (tuple): Position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get and Set"""
        return self.__size

    @property
    def position(self):
        """Get and Set"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """position of the square
        Args:
            value (tuple): position
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ return the area
        Returns:
            the return value is the area
        """
        return self.__size**2

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for j in range(self.__size):
            [print(" ", end="") for k in range(self.__position[0])]
            [print("#", end="") for l in range(self.__size)]
            print("")
