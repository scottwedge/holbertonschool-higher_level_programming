#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    """ rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """"inicialization constructor"""
        """Call the super class with id"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
