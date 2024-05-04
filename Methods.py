class Student:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        print('Defult Contstructer')

    def info(self):
        print(self.name)
        print(self.age)

    def get_weight(self):
        return self.weight

s1 = Student("Munna Biswas", 23, 62)
s2 = Student('Afsar', 24, 52)

s1.info()
print(s1.get_weight())
s2.info()
print(s2.get_weight())