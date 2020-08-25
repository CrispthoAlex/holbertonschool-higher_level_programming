#!/usr/bin/python3
"""
Script that takes your Github credentials
(username = argv[1], passwd = argv[2])
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    print(requests.get(url, auth=(argv[1], argv[2])).json().get('id'))
