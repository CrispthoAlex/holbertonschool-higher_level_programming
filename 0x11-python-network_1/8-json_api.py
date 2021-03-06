#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) == 1:
        value = {'q': ""}
    else:
        value = {'q': argv[1]}

    try:
        req = requests.post(url, data=value)
        req_json = req.json()

        if req_json:
            id_req = req_json.get('id')
            name_req = req_json.get('name')
            print("[{}] {}".format(id_req, name_req))
        else:
            print("No result")

    except Exception:
        print("Not a valid JSON")
