#!/usr/bin/python3

""" Search and update """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text after each line containing a specific string"""
    with open(filename, mode="r", encoding='utf-8') as file_content:
        lines = file_content.readlines()
    with open(filename, mode="w", encoding='utf-8') as file_content:
        for line in lines:
            file_content.write(line)
            if search_string in line:
                file.write(new_string + '\n')
