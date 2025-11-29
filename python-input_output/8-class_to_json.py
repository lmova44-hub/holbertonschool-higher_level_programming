#!/usr/bin/python3
"""Module 8-class_to_json: converts class instance to dictionary"""


def class_to_json(obj):
    """
    Returns the dictionary description of a class instance.
    Only serializable attributes are included.
    """
    return obj.__dict__.copy()
