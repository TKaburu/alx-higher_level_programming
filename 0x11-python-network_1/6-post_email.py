#!/usr/bin/python3

"""
Sends a POST request with the email as a parameter
and displays the body of the response using request package
"""

import sys
import requests


if __name__ == "__main__":

    response = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(response.text)
