#!/usr/bin/python3
"""Defines the add_attribute function"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if it’s possible

    Args:
        obj (any): object to add an attribute
        attr (str): name of the attribute to add to the object
        value (any): value of attr

    Raises:
        TypeError: If the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
