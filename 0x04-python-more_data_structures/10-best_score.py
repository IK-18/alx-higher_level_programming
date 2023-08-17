#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    res = None
    if a_dictionary:
        for i in list(a_dictionary):
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                res = i
    return res
