#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user"""
import requests
import sys


if __name__ == "__main__":
    datum = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": datum}
    res = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        resp = res.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
