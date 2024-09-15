# Object- oriented programming system
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("pooja")
print(s1.name)
del s1.name
print(s1.name)        

# 
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass) 

acc1 = Account("12345", "abcsd")
print(acc1.acc_no)
print(acc1.reset_pass())           

# 
class Person:
    __name = "anonymous"
    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()
p1 = Person()     
print(p1.welcone)       



# inheritance when one class(child / derived) the properties and methods of another class9parent/base)


#  Inheritance
# Type 
# 1. single inheritance 

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("ca stopped..")   

class ToyotaCar(Car):
  def __init__(self, name):
      self.name = name
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.color)


# 2. multi level inheritance 


class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")   

class ToyotaCar(Car):
  def __init__(self, brand):
      self.brand = brand
   
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")        
car1.start()





# 3. multiple inheritance

class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A, B):
    varC = "welcome to class C"        

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)



# Super method

class Car :
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started..")    
    
    @staticmethod
    def stop():
        print("car stopped.")

        class ToyotaCar(Car):
            def __inti__(self, name, type):
                self.name = name
                super().__init__(type)
car1 = ToyotaCar ("prius", "electric")
print(car1.type)              


# class method
class Person:
    name = "anonymous"

def changeName(self, name):
   Person.name = name


p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)    






