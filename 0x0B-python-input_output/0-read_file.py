#!/usr/bin/python3

""" Read a text file """


def read_file(filename=""):
    """ This function reads a text file """
    with open(filename, encoding="utf-8") as file_content:
        file_read = file_content.read().strip()
        print(file_read)
