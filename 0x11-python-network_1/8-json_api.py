#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    try:
        if argv[1] == "":
            value = {'q': ""}
        else:
            value = {'q': argv[1]}

            req = requests.post(url, data=value)
            req_json = req.json()
            id_req = req_json.get('id')
            name_req = req_json.get('name')

        if req_json is {} or (id_req is None or name_req is None):
            print("No result")
        else:
            print("[{}] {}".format(id_req, name_req))

    except Exception:
        print("Not a valid JSON")
