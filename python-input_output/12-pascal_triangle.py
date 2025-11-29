#!/usr/bin/python3
"""Module 11-student: defines Student class with serialization/deserialization"""


class Student:
    """Student class with public attributes and JSON serialization"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.
        If attrs is a list of strings, only include these attributes.
        Otherwise, include all attributes.
        """
        if attrs is None:
            return self.__dict__.copy()
        else:
            filtered = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered[key] = self.__dict__[key]
            return filtered

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from json dict.
        Assume json is a dictionary with valid public attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
