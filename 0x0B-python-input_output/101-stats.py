#!/usr/bin/python3
"""Defines the stats function"""


def stats(size, codes):
    """Reads stdin line by line and computes metrics

    Prints the following stats after every 10 lines
    or keyboard interruption:
    -Total file size up to that point
    -Count of read status codes up to that point
    
    Args:
        size (int): total read file size
        codes (dict): count of status codes
    """
    print("File size: {}".format(size))
    for key in sorted(codes):
        print("{}: {}".format(key, codes[key]))


if __name__ == "__main__":
    import sys


    size = 0
    codes = {}
    valid = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                stats(size, codes)
                count = 1
            else:
                count += 1
            line = line.split()
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass
            try:
                if line[-2] in valid:
                    if codes.get(line[-2], -1) == -1:
                        codes[line[-2]] = 1
                    else:
                        codes[line[-2]] += 1
            except IndexError:
                pass
        stats(size, code)
    except KeyboardInterrupt:
        stats(size, codes)
        raise
