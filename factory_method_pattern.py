"""
Learn how to create simple factory which helps to hide
logic of creating objects.
"""

from abc import ABCMeta, abstractmethod

class AbstractDegree(metaclass=ABCMeta):
    @abstractmethod
    def info(self):
        pass


class BE(AbstractDegree):
    def info(self):
        print("Bachelor of engineering")

    def __str__(self):
        return "Bachelor of engineering"

class ME(AbstractDegree):
    def info(self):
        print("Master of engineering")

    def __str__(self):
        return "Master of engineering"


class MBA(AbstractDegree):
    def info(self):
        print("Master of business administration")

    def __str__(self):
        return "Master of business administration"


class ProfileAbstractFactory(object):
    def __init__(self):
        self._degrees = []

    @abstractmethod
    def createProfile(self):
        pass

    def addDegree(self, degree):
        self._degrees.append(degree)

    def getDegrees(self):
        return self._degrees


class ManagerFactory(ProfileAbstractFactory):
    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(MBA())
        return self._degrees

class EngineerFactory(ProfileAbstractFactory):
    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(ME())
        return self._degrees

class ProfileFactory(object):
    def getProfile(self, factory):
        return factory.createProfile()

    

if __name__ == "__main__":
    pf = ProfileFactory().getProfile(ManagerFactory())
    print(pf)
