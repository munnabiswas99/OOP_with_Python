class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        count = 0
        for val in self.marks:
            sum+=val
            count+=1
        print("hi", self.name, "your average score is ", sum/count)

s1 = Student('Munna Biswas', [80,85,92])
s2 = Student("Habib", [88,76,89])

s1.get_avg()
s2.get_avg()
