#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    args = sys.argv[1:]

    for x in args:
        total += int(x)

    print(total)
