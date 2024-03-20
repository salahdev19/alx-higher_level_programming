#!/usr/bin/python3
""" defines a Student class """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ instance initializer """
        if type(first_name) is not str:
            raise TypeError("first_name must be a string")
        if len(first_name) > 10:
            raise ValueError
        self.first_name = first_name
        if type(last_name) is not str:
            raise TypeError("last_name must be a string")
        if len(last_name) > 10:
            raise ValueError
        self.last_name = last_name
        if age < 0:
            raise ValueError("age cannot be less than 0")
        self.age = age

    def to_json(self, attr=None):
        """ retrives a dictionary representation of Student object """
        if type(attr) is list:
            for item in attr:
                if type(item) is not str:
                    break
            dict_attr = {}
            for key, value in self.__dict__.items():
                if key in attr:
                    dict_attr[key] = value
            return dict_attr
        return self.__dict__
    def reload_from_json(self, json):
        """ replaces all attributes of the Student class """
