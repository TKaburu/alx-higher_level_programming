#!/usr/bin/python3
def element_at(my_list, idx):
    leng = len(my_list)
    if idx >= leng or idx < 0:
        return None
    return my_list[idx]
