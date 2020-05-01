#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nuargv = len(sys.argv) # number of arguments
    add = 0
    if nuargv > 1:
        for i in range(1, nuargv):
            add += int(sys.argv[i])
    print(add)
