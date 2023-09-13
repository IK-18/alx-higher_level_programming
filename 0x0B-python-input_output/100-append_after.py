#!/usr/bin/python3
"""Defines the append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
    containing a specific string

    Args:
        filename (str): name of file
        search_string (str): string to search for
        new_string (str): string to insert
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
