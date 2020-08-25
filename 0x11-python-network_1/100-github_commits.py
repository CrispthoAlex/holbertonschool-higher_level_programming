#!/usr/bin/python3
"""
* Script that list 10 commits (from the most recent to oldest) of the repository
rails by the user rails
* Using the Github API, here is the documentation:
   https://developer.github.com/v3/repos/commits/
* Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
from sys import argv


if __name__ == "__main__":

    repo = argv[1]
    user = argv[2]
    # GET /repos/:owner/:repo/commits
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)
    req = requests.get(url)

    try:
        req_json = req.json()
        # print(req_json)
        if req_json:  # and req_json.get('message') is not 'Not Found':
            count = 0
            for commit in req_json:
                print(commit)
                if count == 10:  # check number of results
                    break
                    count += 1
                sha_repo = commit.get('sha')
                user_name = commit.get('commit').get('author').get('name')
                print("{}: {}".format(sha_repo, user_name))
        else:
            print("No result")
            exit()

    except ValueError:
        print("Not a valid JSON")
        exit()
