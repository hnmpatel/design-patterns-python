'''
Facade design pattern
'''
class Cook(object):
    '''
    Facade class
    Desc: Provides easy interface to prepare dish instead of calling three
          different classes and making difficult for client to use.
    '''
    def prepareDish(self):
        self.cutter = Cutter()
        self.cutter.cutVegetables()

        self.boiler = Boiler()
        self.boiler.boilVegetables()

        self.frier = Frier()
        self.frier.fry()


class Cutter(object):
    '''
    System class
    Desc: Cutter class provide feature of cutting vegetables
    '''
    def cutVegetables(self):
        print("All vegetables are cut")


class Boiler(object):
    '''
    System class
    Desc: Cutter class provide feature of boiling vegetables
    '''
    def boilVegetables(self):
        print("All vegetables are boiled")


class Frier(object):
    '''
    System class
    Desc: Cutter class provide feature of frying vegetables
    '''
    def fry(self):
        print("All vegetables is mixed and fried.")


if __name__ == "__main__":
    # Using facade class to prepare dish
    cook = Cook()
    cook.prepareDish()