#!/bin/bash
# takes in a URL, sends a request to it, and displays the size of the response
curl -s "$1" | wc -c
