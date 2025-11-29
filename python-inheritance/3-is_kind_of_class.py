#!/usr/bin/python3
"""
Module 3-is_kind_of_class

Contains a function that checks if an object is an instance of a class,
or if the object is an instance of a subclass of the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or subclass, else False"""
    return isinstance(obj, a_class)
