#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy_list = my_list[:]
    for t in range(len(cpy_list)):
        if cpy_list[t] == search:
            cpy_list[t] = replace
    return cpy_list
