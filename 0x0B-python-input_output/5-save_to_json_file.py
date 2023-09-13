#!/usr/bin/python3
"""Defines the save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file

    Args:
        my_obj (any): object to save to file
        filename (str): name of file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
