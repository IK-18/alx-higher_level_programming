#!/usr/bin/python3
"""Defines the pascal_triangle function"""


def pascal_triangle(n):
    """Implements a Pascal triangle

    Args:
        n (int): size of Pascal triangle

    Returns:
        a list of lists of integers to represent the triangle
    """
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        tmp = [1]
        for i in range(len(triangle) - 1):
            tmp.append(triangle[i] + triangle[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
