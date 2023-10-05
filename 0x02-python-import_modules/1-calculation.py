#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    add_nums = add(a, b)
    sub_nums = sub(a, b)
    multi_nums = mul(a, b)
    div_nums = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, add_nums))
    print("{:d} - {:d} = {:d}".format(a, b, sub_nums))
    print("{:d} * {:d} = {:d}".format(a, b, multi_nums))
    print("{:d} / {:d} = {:d}".format(a, b, div_nums))
