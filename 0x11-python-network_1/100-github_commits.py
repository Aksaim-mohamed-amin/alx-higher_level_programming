#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of a repository
"""

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)
    if response.status_code == 200:
        for cm in response.json()[:10]:
            print("{}: {}".format(cm['sha'], cm['commit']['author']['name']))
    else:
        print("Error:", response.status_code)
