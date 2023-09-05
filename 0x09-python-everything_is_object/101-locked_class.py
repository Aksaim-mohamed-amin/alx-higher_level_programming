#!/usr/bin/python3
""" LockedClass Class """


class LockedClass:
    """ LockedClass
    prevent the user from initiating new instance with an atributes except
    'first_name'
    """
    __slots__ = ["first_name"]
