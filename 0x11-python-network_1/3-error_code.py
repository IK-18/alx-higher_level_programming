#!/usr/bin/python3
"""sends a request to a URL and diplays the hody of the response"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
