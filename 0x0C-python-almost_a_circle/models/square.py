#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Write the class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """"inicialization constructor"""
        """Call the super class with id"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Get and Set"""
        return self.width

    @size.setter
    def size(self, value):
        """Get and Set"""
        self.width = value
        self.height = value

    def __str__(self):
        """should print, and str() should return"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") " + \
            str(self.x) + "/" + str(self.y) + " - " + \
            str(self.width)
        return string

    def update(self, *args, **kwargs):
        """ update test"""
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            elif i == 1:
                self.size = j
            elif i == 2:
                self.x = j
            elif i == 3:
                self.y = j
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """ dictionary test"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
