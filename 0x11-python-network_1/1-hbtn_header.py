#!/usr/bin/python3
"""
takes a URL, sends a request to it and displays the value of the X-Request-Id
"""

import sys
import urllib.request


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(dict(response.headers).get('X-Request-Id'))
