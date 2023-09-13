#!/usr/bin/python3
"""Defines the function to_string_json"""
import json


def from_json_string(my_str):
    """Implements the object (Python data structure)
    represented by a JSON string

    Args:
        my_str (str): string to be parsed

    Returns:
        object (Python data structure) representation of my_str
    """
    return json.loads(my_str)
