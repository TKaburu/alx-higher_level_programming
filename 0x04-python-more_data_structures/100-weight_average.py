#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_t = 0
    weight = 0
    for item in my_list:
        sum_t = sum_t + (item[0] * item[1])
        weight = weight + item[-1]
    return sum_t / weight
