#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Contains a function that checks if an object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or subclass, otherwise False"""
    return isinstance(obj, a_class)
