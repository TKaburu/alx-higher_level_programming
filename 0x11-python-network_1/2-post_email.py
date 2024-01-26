#!/usr/bin/python3

"""
Sends a POST request with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')

with urllib.request.urlopen(sys.argv[1], data=data) as response:
    content = response.read().decode('utf-8')
    print(content)
