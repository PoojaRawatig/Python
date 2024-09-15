print("hello world")

# variables

name = "pooja"
age = 23
price = 34.55
print(type (name))
print (" my name is : ", name)
print (" my name is : ", age)

# Data types

# integers -ve, +ve, o
# string "pooja" , "hello"
# float 3.99, 2.4, 9.0
# boolean True, False
# none a=none
age = 23
old = True
a = None

print(type(old))
print(type(a))

#  print sum fo 2 number

a = 100
b= 500
sum = a + b
print(sum)


# types of operators

#arithmetic operator
# a = 5
# b = 2

print( a  + b)
print( a - b)
print( a / b)
print( a  * b)
print( a  % b)
print( a ** b)

#Relational comparison operator
a =  40
b = 30

print(a == b)
print(a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)

#Assignment operators

num = 10
num /= 5
num += 5
num %= 5
num -= 5
num **= 5
print("num : ", num) 

#Logical operators
a = 50
b = 30
print(not False)
print(not True)
print(not (a > b))


#and operator
val1 = True
val2 = True

print("AND operator: ", val1 and val2)
print("OR operator: ", val1 or val2)
print("OR operator: ", (a == b ) or (a > b))


# Type Conversion

a = "2"
b = 4.25
sum = a + b 
print(sum)

a = float("2")
b = 4.25
print(type(a))
print( a + b)

a = 3.14
a = str(a)
print(type(a))


# input in python
input() #int 1


name = input ("enter your age:")
print(" you entered", name)

int(input()) #int 2
val = input("enter some value: ")
print(type(val), val)


float(input()) #float 3
int("5")
val = int(input("Enter some value"))
print(type(val, val))


name = input("enter name: ")
age = int(input("enter age"))
marks = float(input("enter marks"))


print('welcome',name)
print("age =", age)
print("marks =", marks)


