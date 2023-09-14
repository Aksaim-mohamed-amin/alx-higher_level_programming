#!/usr/bin/python3
""" Student Class """


class Student:
    """ Define a class student """
    def __init__(self, first_name, last_name, age):
        """ Initialize a new instance of student class

        Args:
          fisr_name: Student fisrt name.
          last_name: Student last name.
          age: Student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return a dictionary representation of a Student instance

        Args:
          attrs: list of the attributes to return if None return all.
        """
        if attrs is None:
            return (self.__dict__)
        return {atr: getattr(self, atr) for atr in attrs if hasattr(self, atr)}
