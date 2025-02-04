#Welcome 
class Student:
    """This class is developed by Shivani for Demo purpose"""
    
print(Student.__doc__)
help(Student)
 #Example on methods and object creation
class Student:
    def __init__(self):
        print("constructor execution...")
        self.name="Shivani"
        self.age=19
        self.rno=204
    def talk(self):
        print("My name is:",self.name)
        print("My age is:",self.age)
        print("My rno is:",self.rno)
s=Student()
s.talk()
print(s.name)
print(s.age)
print(s.rno)
s1=Student()
s2=Student()
#Constructor is executed 2 times beacause of two different objects
