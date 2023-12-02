#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
