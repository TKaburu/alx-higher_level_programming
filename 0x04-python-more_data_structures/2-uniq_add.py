#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    res = 0
    for t in new_list:
        res = res + 1
    return res
