#!/usr/bin/python3
"""
Function that returns a dictionary description of an object
for JSON serialization.
"""

def class_to_json(obj):
    """
    Args:
        obj: an instance of a class
    Returns:
        dictionary of all serializable attributes of obj
    """
    return obj.__dict__
