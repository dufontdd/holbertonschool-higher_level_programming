#!/usr/bin/python3
"""
Module that defines a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): the matrix to divide
        div (int/float): the divisor

    Returns:
        list: a new matrix with elements divided and rounded to 2 decimals

    Raises:
        TypeError: if matrix elements are not int/float or rows have different sizes
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
    """
    # Check div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check matrix
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(el, (int, float)) for row in matrix for el in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check all rows have the same size
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Create new matrix with rounded division
    new_matrix = [[round(el / div, 2) for el in row] for row in matrix]

    return new_matrix
