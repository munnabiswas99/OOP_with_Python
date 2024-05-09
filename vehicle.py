from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, wheel):
        self.wheel = wheel

    @abstractmethod
    def start(self):
        pass

    def display(self):
        print('Callig from vehicle class')