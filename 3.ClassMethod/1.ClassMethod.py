class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def printStudent(self):
        print(self.name)
        print(self.rollno)
        
    @classmethod # this method is used to return a object of class type
    def getStudent(cls, name, rollno):
        return cls(name, rollno)
        
        
s1 = Student("Max", 10)
s2 = Student("John", 20)
# s1.printStudent()
s3 = Student.getStudent("Peter", 33)

print(s3.name)
print(s3.rollno)