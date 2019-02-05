"""
Learn how to create simple factory which helps to hide
logic of creating objects.
"""
"""
Provide an interface for creating families of related or dependent
objects without specifying their concrete classes.
"""

from abc import ABCMeta, abstractmethod


class CarFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def build_parts(self):
        pass

    @abstractmethod
    def build_car(self):
        pass


class SedanCarFactory(CarFactory):

    def build_parts(self):
        return SedanCarParts()

    def build_car(self):
        return SedanCar()


class SUVCarFactory(CarFactory):

    def build_parts(self):
        return SUVCarParts()

    def build_car(self):
        return SUVCar()


class CarParts(metaclass=ABCMeta):
    """
    Declare an interface for a type of car parts.
    """

    @abstractmethod
    def build(self):
        pass


class SedanCarParts(CarParts):

    def build(self):
        print("Sedan car parts are built")


class SUVCarParts(CarParts):

    def build(self):
        print("SUV Car parts are built")


class AbstractCar(metaclass=ABCMeta):
    """
    Declare an interface for a type of cars.
    """

    @abstractmethod
    def assemble(self):
        pass


class SedanCar(AbstractCar):

    def assemble(self, parts):
        print(f"Sedan car is assembled here using {parts}")


class SUVCar(AbstractCar):

    def assemble(self, parts):
        print(f"SUV car is assembled here using {parts}")


if __name__ == "__main__":
    for factory in (SedanCarFactory(), SUVCarFactory()):
        car_parts = factory.build_parts()
        car_builder = factory.build_car()
        car_parts.build()
        car_builder.assemble(car_parts)