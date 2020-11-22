'''
Template method Pattern - This is behavioral design pattern.
'''
import abc


class ThreeDaysTrip(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def transport(self):
        pass

    @abc.abstractmethod
    def day1(self):
        pass

    @abc.abstractmethod
    def day2(self):
        pass

    @abc.abstractmethod
    def day3(self):
        pass

    @abc.abstractmethod
    def back_to_home(self):
        pass

    def iternary(self):
        print("Trip is started")
        self.transport()
        self.day1()
        self.day2()
        self.day3()
        self.back_to_home()
        print("Trip is over")


class SouthTrip(ThreeDaysTrip):
    def transport(self):
        print("Go by train! check in to hotel")

    def day1(self):
        print("Day-1: Enjoy the hotel beach whole day")

    def day2(self):
        print("Day-2: Visit historical places and Enjoy cruise life at night")

    def day3(self):
        print("Day-3: Enjoy shopping day with family and go anywhere you wish")

    def back_to_home(self):
        print("Check out and go Home by air!")


class NorthTrip(ThreeDaysTrip):
    def transport(self):
        print("Go by air! check in to hotel")

    def day1(self):
        print("Day-1: Go to very highted place and enjoy snow activities")

    def day2(self):
        print("Day-2: Enjoy river rafting and lavish dinner at night")

    def day3(self):
        print("Day-3: Enjoy shopping day with family and go anywhere you wish")

    def back_to_home(self):
        print("Check out and go Home by air!")


if __name__ == "__main__":
    place = input("Where do you want to go? ")
    if place == 'north':
        trip = NorthTrip()
        trip.iternary()
    elif place == 'south':
        trip = SouthTrip()
        trip.iternary()
    else:
        print("Sorry, We do not have any trip towards that place!")