#!/usr/bin/env python3
"""Module multiply matrix"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists.
        ValueError: If m_a or m_b is empty or if matrices cannot be multiplied.

    python3 
        TypeError: m_a should contain only integers or floats
    """
    
    if not isinstance(m_a, list) or not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    if len(m_a) == 0 or any(len(row) != len(m_a[0]) for row in m_a):
        raise ValueError("m_a can't be empty or must be a rectangle")
    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not isinstance(m_b, list) or not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")
    if len(m_b) == 0 or any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("m_b can't be empty or must be a rectangle")
    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        result.append(row)

    return result






    
    