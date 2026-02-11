#!/usr/bin/python3
"""
Defines a Student class with JSON serialization and optional filtering.
"""

class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student.

        If attrs is a list of strings, only those attributes are included.
        Otherwise, return all attributes.
        """
        if attrs is None:
            return self.__dict__.copy()  # retourne tous les attributs
        filtered = {}
        for key in attrs:
            if key in self.__dict__:  # seulement si l'attribut existe
                filtered[key] = self.__dict__[key]
        return filtered
