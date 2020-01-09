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
        return self.position

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
            self.__size = value #: size value

    @position.setter
    def position(self, value):
        """position of the square
        Args:
            value (tuple): position
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value #: position value

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