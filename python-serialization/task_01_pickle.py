#!/usr/bin/env python3
"""Pickling Custom Classes: CustomObject class with serialize/deserialize methods."""

import pickle


class CustomObject:
    """A custom Python object with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject instance.

        Args:
            name (str): Name of the person.
            age (int): Age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object’s attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file using pickle.

        Args:
            filename (str): The filename to save the pickled object.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load a pickled object from a file.

        Args:
            filename (str): The filename to load the pickled object from.

        Returns:
            CustomObject: The deserialized object, or None if failed.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None
