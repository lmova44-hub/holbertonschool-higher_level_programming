#!/usr/bin/python3
"""Module 1-write_file: contains write_file function"""


def write_file(filename="", text=""):
    """Writes text to a UTF-8 file and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
