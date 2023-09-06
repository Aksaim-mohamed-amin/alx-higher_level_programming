#!/usr/bin/python3
""" Define a function that print a formated text. """


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these
    characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")

        if text[c] in ".?:" or text[c] == '\n':
            if text[c] in ".?:":
                print('\n')
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue

        c += 1
