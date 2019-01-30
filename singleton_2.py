"""
Pattern name - SingleTon (Mono state pattern)
Pattern type - Creational Design Pattern
"""

# Solution - 2
class Borg(object):
    _shared = {}

    def __init__(self):
        self.__dict__ = self._shared


class SingleTon(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg

    # def __str__(self):
    #     return "<{} - Object>".format(self.val)


o1 = SingleTon("Hardik")
print("Object - 1 ==>", o1)
print("Object - 1 val ==>", o1.val)

o2 = SingleTon("Aarav")
print("Object - 2 ==>", o2)
print("Object - 2 val ==>", o2.val)
print("Object - 1 val ==>", o1.val)

print(o1.__dict__)
print(o2.__dict__)