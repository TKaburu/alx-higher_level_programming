#!/usr/bin/python3

"""
Sends a POST request with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""

import sys
from urllib import parse, request


if __name__ == "__main__":

    data = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')

    with request.urlopen(sys.argv[1], data) as response:
        content = response.read().decode('utf-8')
        print(content)
