#!/usr/bin/python3
"""Defines the function to_string_json"""
import json


def to_json_string(my_obj):
    """Implements the JSON representation of an object (string)

    Args:
        my_obj (str): string to be parsed

    Returns:
        JSON representation of my_obj
    """
    return json.dumps(my_obj)
