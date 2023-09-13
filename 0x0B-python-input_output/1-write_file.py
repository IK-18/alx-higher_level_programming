#!/usr/bin/python3
"""Defines the write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename (str): name of file
        text (str): text to write to file

    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
