#!/usr/bin/python3
"""Module 3-to_json_string: contains to_json_string function.
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).
    """
    return json.dumps(my_obj)
