from abc import ABC, abstractmethod

class Car(ABC):
    def show(self):
        print("Car has 4 wheels")

    @abstractmethod
    def speed(self):
        pass

class BMW(Car):
    def speed(self):
        print("200 km/h")

class Suzuki(Car):
    def speed(self):
        print("120 km/h")

b1 = BMW()
s1 = Suzuki()

b1.show()
b1.speed()
s1.show()
s1.speed()