#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0
    try:
        for i in range(0, x):
            print(my_list[i], end="")
            element = element + 1
    except:
        pass
    print()
    return element
