#!/usr/bin/python3
"""
fetch https://alx-intrant.hbtn.io/status using requests
and displays the value of the variable X-Request-Id in the response header
"""

import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print(r.headers.get('X-Request-Id'))
