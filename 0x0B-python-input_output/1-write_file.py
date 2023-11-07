#!/usr/bin/python3

""" Write a string to a text file """


def write_file(filename="", text=""):
    """
    Args:
        Filename: The file
        Text: The text
        Reurn: The number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file_content:
        file_char = file_content.write(text)
        return (file_char)
