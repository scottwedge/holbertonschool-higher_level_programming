#!/usr/bin/python3
""" Write a
    function
    that
    adds 2 integers.
    """


def add_integer(a, b=98):
    """ Prototype: def add_integer(a, b=98):
        Raises:
            TypeError exception with the message a must be an integer or"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    elif ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
