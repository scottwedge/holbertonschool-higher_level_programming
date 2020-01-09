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
            self.__size = value

    @position.setter
    def position(self, value):
        """position of the square
        Args:
            value (tuple): position
        """
        if len(value) == 2:
            if type(value[0]) is int and type(value[1]) is int:
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = (value[0], value[1])
                else:
                    raise TypeError("position must be a tuple of 2 positive integers")
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
