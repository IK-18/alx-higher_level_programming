#!/usr/bin/python3
"""Defines the class_to_join function"""


def class_to_json(obj):
    """Implements the dictionary description of an object

    Args:
        obj (any): the object

    Returns:
        the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean) for
        JSON serialization of an object
    """
    return obj.__dict__
