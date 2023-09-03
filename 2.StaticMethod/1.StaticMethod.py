class Student:
    count = 0
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def printStudent(self):
        print(self.name)
        print(self.rollno)
        
    @staticmethod # this means by default, self will not get passed
    def totalStudent():
        print("Static Method called")
        Student.count += 1
        print("Total number of Students", Student.count)
        
s1 = Student("Max", 10)
s2 = Student("John", 20)
s1.printStudent()

s1.totalStudent()
s2.totalStudent()