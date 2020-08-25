#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":

    repo = argv[1]
    user = argv[2]
    # example
    # GET /repos/:owner/:repo/commits
    url = 'https://api.github.com/repos/{}/{}/commits/'.format(
        user, repo)

    try:
        req = requests.get(url)
        req_json = req.json()
        print(req_json)
        if req_json and req_json.get('message') is not 'Not Found':
            count = 0
            for commit in req_json:
                count += 1
                if count <= 11:
                    break
                sha_repo = commit.get('sha')
                user_name = commit.get('author').get('name')
                print("{}: {}".format(sha_repo, user_name))
        else:
            print("No result")

    except Exception:
        print("Not a valid JSON")
