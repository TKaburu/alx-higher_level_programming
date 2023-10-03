#!/usr/bin/python3
for t in range(0, 9):
    for k in range(t + 1, 10):
        if t == 8:
            print("{:d}{:d}".format(t, k))
            break
        print("{:d}{:d}".format(t, k), end=", ")
