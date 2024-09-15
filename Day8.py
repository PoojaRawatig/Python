class Student:
    name = "karan"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2. name)

class Car:
   color = "blue"  #this is class created 
   brand = "mercedes"


car1 = Car() # this is object created
print(car1.color)
print(car1.brand)


# 
class Student:
 def __init__(self, fullname, marks):
    self.name = fullname
    self.marks = marks
    print("adding new student in database..")
    
    s1 = Student("pooja")
    print(s1.name, s1.marks)

    

