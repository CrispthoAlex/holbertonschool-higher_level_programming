#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8)
"""
import urllib.request
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    # values = {'email': argv[2]}  # dictionary to request
    # data shoulb be bytes
    # data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
