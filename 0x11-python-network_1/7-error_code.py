#!/usr/bin/python3

"""
Sends a request, manages errors exceptions and print error code
using requests package
"""

import sys
import requests


if __name__ == "__main__":

    response = requests.get(sys.argv[1])

    # handle error
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
