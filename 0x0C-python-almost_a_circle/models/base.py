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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file = cls.__name__ + ".json"
        empty = []
        for i in list_objs:
            empty.append(cls.to_dictionary(i))
        with open(file, "w") as w:
            w.write(cls.to_json_string(empty))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            from models.rectangle import Rectangle
            obj = Rectangle(1, 1)
        elif cls.__name__ is "Square":
            from models.square import Square
            obj = Square(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        from os import path

        file = cls.__name__ + ".json"
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        import json

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """json metohd"""
        import json
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
