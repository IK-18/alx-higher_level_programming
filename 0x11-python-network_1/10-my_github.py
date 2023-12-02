#!/usr/bin/python3
"""uses the GitHub API to display your id"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    r = res.json()
    print(r.get("id"))
