#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    new.update(a_dictionary)
    for i in new:
        new[i] *= 2
    return new
