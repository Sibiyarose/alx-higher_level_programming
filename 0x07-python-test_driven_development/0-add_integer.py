#!/usr/bin/python3
"""
Calculates the sum of 2 integers
a and b must be integers or floats
a and b must be first casted to integers if they a float
Return: the addition of a and b
"""

def add_integer(a, b=98):
    """a and b aare integers
    Returns an integer: the addition of a and b
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not (isinstance(a, int)):
        raise TypeError("a must be an interger")
    if not (isinstance(b, int)):
        raise TypeError("b must be an interger")
    return (a + b)
