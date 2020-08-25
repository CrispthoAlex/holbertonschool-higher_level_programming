#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8)
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    # values = {'email': argv[2]}  # dictionary to request
    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
