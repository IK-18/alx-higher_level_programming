#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{} argument{}{}".format(len(argv) - 1,
                                   "" if len(argv) == 2 else "s",
                                   "." if len(argv) <= 1 else ":"))
    for i, j in enumerate(argv[1:]):
        print("{}: {}".format(i + 1, j))
