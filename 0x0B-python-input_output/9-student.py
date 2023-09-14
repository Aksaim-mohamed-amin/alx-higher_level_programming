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

    def to_json(self):
        """ Return a dictionary representation of a Student instance """
        return (self.__dict__)
