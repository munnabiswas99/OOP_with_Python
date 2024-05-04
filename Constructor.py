class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Object is created")

s1 = Student('Munna',22)
s2 = Student("Biswas", 23)

print(s1.name)
print(s2.age)