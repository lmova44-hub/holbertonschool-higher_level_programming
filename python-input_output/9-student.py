#!/usr/bin/python3
"""Module 9-student: defines a Student class with JSON representation"""


class Student:
    """Defines a student with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of Student instance"""
        return self.__dict__.copy()
