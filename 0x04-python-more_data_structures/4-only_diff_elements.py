#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = list(filter(lambda i: i not in set_2, set_1))
    for i in set_2:
        if i not in set_1:
            res.append(i)
    return res
