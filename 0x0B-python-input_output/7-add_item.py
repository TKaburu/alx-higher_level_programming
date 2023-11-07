#!/usr/bin/python3

""" import json and sys """


import json
import sys


""" import previous functions """

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    from_json = load_from_json_file('add_item.json')
except FileNotFoundError:
    from_json = []

arguments = sys.argv[1:]
from_json.extend(arguments)
save_to_json_file(from_json, 'add_item.json')
