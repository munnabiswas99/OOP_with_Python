class Student:
    def __init__(self,name,age,id):
        self.name = name
        self._age = age
        self.__id = id

    def set_id(self,id):
        self.__id = id
    
    def get_id(self):
        return self.__id
    
s1 = Student('Munna', 22, 5261)
print(s1.name, s1._age)

s1.set_id(5566)
print(s1.get_id())

class Munna(Student):
    pass

m1 = Munna('Munna', 22, 5261)
print(m1._age)