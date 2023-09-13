#!/usr/bin/python3
"""Defines the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates an object from a "JSON file"

    Args:
        filename (str): name of file

    Returns:
        created object
    """
    with open(filename) as f:
        return json.load(f)
