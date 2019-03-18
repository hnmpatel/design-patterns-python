class Cook(object):
    def prepareDish(self):
        self.cutter = Cutter()
        self.cutter.cutVegetables()

        self.boiler = Boiler()
        self.boiler.boilVegetables()

        self.frier = Frier()
        self.frier.fry()


class Cutter(object):
    def cutVegetables(self):
        print("All vegetables are cut")


class Boiler(object):
    def boilVegetables(self):
        print("All vegetables are boiled")


class Frier(object):
    def fry(self):
        print("All vegetables is mixed and fried.")


if __name__ == "__main__":
    cook = Cook()
    cook.prepareDish()