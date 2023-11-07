#!/usr/bin/python3

""" Append text to file """


def append_write(filename="", text=""):
    """
    This function appends text to file and
    returns number of characters
    """
    with open(filename, mode="a", encoding="utf-8") as file_content:
        return (file_content.write(text))
