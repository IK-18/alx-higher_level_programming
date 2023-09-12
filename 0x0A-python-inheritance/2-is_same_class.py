#!/usr/bin/python3
"""Defines the is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if an the object is exactly an instance
    of teh specified class

    Args:
        obj (any): object whose type is to be checked
        a_class (type): object type

    Returns:
        True if the object is exactly an instance of the specified class
        False otherwise
    """
    return type(obj) == a_class
