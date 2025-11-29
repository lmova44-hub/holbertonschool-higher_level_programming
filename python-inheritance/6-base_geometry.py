#!/usr/bin/python3
"""
Module 6-base_geometry
Contains a class BaseGeometry with an area() method
that raises an Exception
"""


class BaseGeometry:
    """Base class for geometry shapes"""

    def area(self):
        """Raise an exception because area() is not implemented"""
        raise Exception("area() is not implemented")
