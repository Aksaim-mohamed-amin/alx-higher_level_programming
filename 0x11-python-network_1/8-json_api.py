#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

import sys
import requests

if __name__ == "__main__":

    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        data = response.json()

        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")

    except requests.HTTPError as error:
        print("Error:", error)

    except ValueError:
        print("Not a valid JSON")
