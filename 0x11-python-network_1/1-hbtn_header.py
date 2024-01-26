#!/usr/bin/python3

"""
Sends a request to the specified URL and displays the value of
the X-Request-Id variable in the header of the response
"""

import sys
import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)
