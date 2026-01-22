#!/usr/bin/python3
"""Unittests for max_integer function"""
import unittest
import sys
sys.path.append('..')  # permet d'importer le fichier parent

from 6_max_integer import max_integer  # Nom du fichier sans tiret

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 5, 3]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_same_values(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

if __name__ == "__main__":
    unittest.main()
