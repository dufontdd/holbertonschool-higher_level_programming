#!/usr/bin/python3
"""Module that prints a text with 2 new lines after '.', '?' and ':'"""


def text_indentation(text):
    """Prints text with 2 newlines after '.', '?', ':'.

    Args:
        text (str): The text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Les caractères de séparation
    separators = ['.', '?', ':']
    start = 0  # début de la sous-chaîne

    for i, char in enumerate(text):
        if char in separators:
            # Extraire la sous-chaîne et enlever les espaces de début et fin
            piece = text[start:i + 1].strip()
            if piece:
                print(piece)
                print()
            start = i + 1

    # Si reste de texte après la dernière séparation
    remainder = text[start:].strip()
    if remainder:
        print(remainder)
