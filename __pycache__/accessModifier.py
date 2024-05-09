class Student:
    def __init__(self, name, age, roll):
        self.name = name
        self._age = age
        self.__roll = roll
    def display1(self):
        print("This is public function") #Accessible from everywhere
    
    def _display2(self):
        print("This is a Proctected function") # Accessible from derived class

    def __display3(self):
        print('This is a private method') # Accessible within own class

class Info(Student):
    st = Student("Munna", 22, 5261)
    st._display2()

s1 = Info('Munna', 22, 5261)

print(s1.name)
# print(s1._age) # attribute error
# print(s1.__roll)  # attribute error

s1.display1()
# s1.display2() # attribute error
# s1.display3() #attributr error

