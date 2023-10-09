def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_num = my_list[0]
    for t in my_list:
        if t > max_num:
            max_num = t
    return max_num
