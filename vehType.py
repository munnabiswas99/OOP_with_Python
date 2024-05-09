from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, wheel, color):
        super().__init__(wheel)
        self.color = color

    def start(self):
        print("Bike started with kick")

class Car(Vehicle):
    def __init__(self, wheel, color):
        super().__init__(wheel)
        self.color = color

    def start(self):
        print("Car started with key")