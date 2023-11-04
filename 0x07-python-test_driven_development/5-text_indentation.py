#!/usr/bin/python3
"""
a function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """Defining the function"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delimeter in ".:?":
        text = (delimeter + "\n\n").join(
            [line.strip(" ") for line in text.split(delimeter)])

    print(f"{text}", end="")
