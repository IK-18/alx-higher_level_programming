#!/usr/bin/python3
"""Defines the append_write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
        filename (str): name of file
        text (str): text to append to file

    Returns:
        number of characters written
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
