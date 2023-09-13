#!/usr/bin/python3
"""Defines the read-file function"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): name of file to be read
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
