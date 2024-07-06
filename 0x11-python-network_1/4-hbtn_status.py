#!/usr/bin/env python3
import requests

# URL to fetch
url = 'https://alx-intranet.hbtn.io/status'

# Fetch the URL
response = requests.get(url)

# Display the body response
print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")
