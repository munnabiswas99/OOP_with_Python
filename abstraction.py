class Car:
    def __init__(self):
        self.brk = False
        self.acc = False
        self.clutch = False
    
    def start(self):
        self.brk = True
        self.acc = True
        self.cluth = True
        print('Car is started')

c1 = Car()
c1.start()