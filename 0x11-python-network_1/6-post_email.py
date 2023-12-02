#!/usr/bin/python3
"""sends a request to a URL and diplays the hody of the response"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    res = requests.post(url, data=data)
    print(res.text)
