#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv) - 1
    arg_res = 0
    for t in range(leng):
        arg_res += int(sys.argv[t + 1])
    print("{}".format(args_res))
