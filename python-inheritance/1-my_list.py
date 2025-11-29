#!/usr/bin/python3
"""
Module 1-my_list
Contains a class MyList that inherits from list
and has a method to print a sorted list
"""


class MyList(list):
    """A list subclass with an additional method to print a sorted list"""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list"""
        print(sorted(self))
