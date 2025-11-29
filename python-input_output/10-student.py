#!/usr/bin/python3
"""Module 10-student: defines a Student class with filtered JSON representation"""


class Student:
    """Defines a student with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student instance

        If attrs is a list of strings, only include attributes in that list.
        Otherwise, include all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()
