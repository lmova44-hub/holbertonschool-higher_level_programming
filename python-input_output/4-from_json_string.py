#!/usr/bin/python3
"""Module 4-from_json_string: contains from_json_string function.
"""
import json


def from_json_string(my_str):
    """
    Return the Python object represented by a JSON string.
    """
    return json.loads(my_str)
