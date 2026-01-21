#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Utilise list comprehension pour créer une nouvelle matrice
    return [[x ** 2 for x in row] for row in matrix
