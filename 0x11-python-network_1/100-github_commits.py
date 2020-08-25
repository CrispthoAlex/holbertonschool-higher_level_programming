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
    # https://api.github.com/repos/octocat/Hello-World/git/commits/
    url = 'https://api.github.com/repos/{}/{}/git/commits/'.format(
        user, repo)

    try:
        req = requests.get(url)
        req_json = req.json()

        if req_json:
            count = 0
            for commit in req_json:
                count += 1
                if count == 10:
                    break
                sha_repo = commit.get('sha')
                user_name = commit.get('author').get('name')
                print("{}: {}".format(sha_repo, user_name))
        else:
            print("No result")

    except Exception:
        print("Not a valid JSON")
