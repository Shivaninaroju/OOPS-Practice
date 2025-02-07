#Day-1 
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
s=Student()  #Creating 's' reference variable
s.talk()
print(s.name)
print(s.age)
print(s.rno)
s1=Student()
s2=Student()
#Constructor is executed 2 times beacause of two different objects
print(id(s1))
print(id(s2))

#Day-2
##To execute multiple students information
class Student:
    def __init__(self,name,age,rno):   ##Self is reference variable pointing to current object and used to access obj values inside class.
        self.name=name
        self.age=age
        self.rno=rno
    def talk(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Rno:",self.rno)
s1=Student("shivani",19,204)
s2=Student("Niveditha",18,205)
s3=Student("Kavya",18,206)
s1.talk()
s2.talk()
s3.talk()
