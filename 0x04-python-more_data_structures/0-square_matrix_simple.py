#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        i = list(map(lambda x: x * x, i))
        new.append(i)
    return new
