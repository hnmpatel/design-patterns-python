"""
Learn how to create simple factory which helps to hide
logic of creating objects.
"""

from abc import ABCMeta, abstractmethod

class Degree(metaclass=ABCMeta):
    @abstractmethod
    def info(self):
        pass


class BE(Degree):
    def info(self):
        print(f"Bachelor of engineering")


class ME(Degree):
    def info(self):
        print(f"Master of engineering")


class MBA(Degree):
    def info(self):
        print(f"Master of business administration")


class ProfileFactory(object):
    def __init__(self):
        self._degrees = []

    @abstractmethod
    def createProfile(self):
        pass

    def addDegree(self, degree):
        self._degrees.append(degree)

    def getDegrees(self):
        return self._degrees


class Manager(ProfileFactory):
    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(MBA())

class Engineer(ProfileFactory):
    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(ME())


if __name__ == "__main__":
    profile = input("Please create profile from Engineering or Manager - ")
    p = eval(profile)()
    p.createProfile()
    print(p.getDegrees())
