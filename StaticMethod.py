class Student:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    @staticmethod   #Decorator
    def dept():
        print("CSE")

s1 = Student('Munna',22)
print(s1.name)
s1.dept()