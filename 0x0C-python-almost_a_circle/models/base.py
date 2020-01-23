#!/usr/bin/python3
"""Write the first class Base:"""


class Base:
    """Class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Inicialice class"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
