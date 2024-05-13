class Human:
    def __init__(self,eye,leg):
        self.eye = eye
        self.leg = leg

    def eat(self):
        print('I can eat')

    def work(self):
        print("I can walk")

class Male(Human):
    def __init__(self, nose, eye, leg):
        super().__init__(eye, leg)
        self.nose = nose

    def play(self):
        print('I play football')

    def work(self): #Method Overridding
        super().work() #calling parent class method
        print('I can play guiter')

m1 = Male(1,2,2)
m1.eat()
m1.work()
print(m1.eye)
print(m1.leg)
print(m1.nose)
