#!/usr/bin/python3
"""
Returns True if the object is an instance of a class that inherited
from the specified class.
"""


def inherits_from(obj, a_class):
    """Check if obj is instance of a subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
