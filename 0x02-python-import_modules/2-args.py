#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg = len(sys.argv) - 1
    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg))
    for t in range(arg):
        print("{}: {}".format(t + 1, sys.argv[t + 1]))
