"""
Learn how to create simple factory which helps to hide
logic of creating objects.
"""

from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

class HR(Person):
    def create(self, name):
        print(f"HR {name} is created")

class Engineer(Person):
    def create(self, name):
        print(f"Engineer {name} is created")

class PersonFactory(object):
    @classmethod
    def createPerson(cls, designation, name):
        eval(designation)().create(name)


if __name__ == "__main__":
    designation = input("Please enter the designation - ")
    name = input("Please enter the person's name - ")
    PersonFactory.createPerson(designation, name)
