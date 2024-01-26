#!/usr/bin/python3

"""
Sends a request, manages errors exceptions and print error code 
"""

import sys
from urllib import request, error


if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as response:
            content = response.read().decode('utf-8')
            print(content)

    except error.HTTPError as e:
        print(f"Error code: {e.code}")
