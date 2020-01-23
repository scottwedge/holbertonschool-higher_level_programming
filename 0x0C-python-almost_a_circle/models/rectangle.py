#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """"inicialization constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """Call the super class with id"""
        super().__init__(id)

    @property
    def width(self):
        """Get and Set"""
        return self.__width

    @width.getter
    def width(self, value):
        """Set value
        Args:
            value (int): width of the rectangle
        """
        self.__width = value

    @property
    def height(self):
        """Get and Set"""
        return self.__height

    @height.getter
    def height(self, value):
        """Set value
        Args:
            value (int): height of the rectangle
        """
        self.__height = value

    @property
    def x(self):
        """Get and Set"""
        return self.__x

    @x.getter
    def x(self, value):
        """Set value
        Args:
            value (int): x of the rectangle
        """
        self.__x = value

    @property
    def y(self):
        """Get and Set"""
        return self.__y

    @y.getter
    def y(self, value):
        """Set value
        Args:
            value (int): y of the rectangle
        """
        self.__y = value
