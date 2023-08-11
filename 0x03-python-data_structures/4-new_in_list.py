#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp = my_list.copy()
    tmp[idx] = element
    return tmp
