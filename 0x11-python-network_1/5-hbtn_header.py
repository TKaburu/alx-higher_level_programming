#!/usr/bin/python3

"""
Sends a request to the specified URL and displays the value of
the X-Request-Id variable in the header of the response
"""

import sys
import requests


if __name__ == "__main__":

    response = requests.get(sys.argv[1])
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
