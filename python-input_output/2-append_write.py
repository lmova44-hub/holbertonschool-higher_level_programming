#!/usr/bin/python3
"""Module 2-append_write: contains the append_write function.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a UTF-8 text file and return
    the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
