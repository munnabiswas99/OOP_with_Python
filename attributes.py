class Car:
    brand = 'Unknown'

    def __init__(self, brand):
        self.brand = brand

c1 = Car("BMW")
c2 = Car('x')

print(c1.brand)
print(c2.brand)