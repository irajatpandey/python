class Student:
    
    def __init__(self, name, rollno):
        self.__name = name # by putting __ before the variale, it becomes private
        self.rollno = rollno
    def printStudent(self):
        print(self.name)
        print(self.rollno)
    
        
        
s1 = Student("Max", 10)
s2 = Student("John", 20)

print(s1.name) # it will throw an error, since name is private