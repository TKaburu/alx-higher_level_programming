#!/usr/bin/python3
for t in range(97, 123):
    if chr(t) != 'e' and chr(t) != 'q':
        print("{:c}".format(t), end="")
