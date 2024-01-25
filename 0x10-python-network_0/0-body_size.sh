#!/bin/bash
# a Bash script that takes in a URL and send a request to it
curl -s "$1" | wc -c
