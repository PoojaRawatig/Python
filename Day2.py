# String 
str1 = "This is a string"
# str2 = 'welcome'
# str3 = """this is a string"""
print(str1)

# lenght
str2 = 'welcome'
len2 = len(str2)
print(len2)

# concatination
final_str = str1 + " "  +  str2
print(final_str)
print(len(final_str))

# indexing
str = "Pooja Rawat"
print(str[3])

# slicing

str = "Pooja Rawat"
print(str[1:4])

# starting and endwith

str = "i am studying python from apnacollege"
print(str.endswith("ege"))


# capitalizes 1st char
str = "i am studying python from apnacollege"
print(str.capitalize())
print(str)


# replaces all accurrences of old
str = "i am studying python from apnacollege"
print(str.replace("python", "javascript"))

# return 1st index of 1st occurrer
str = "i am from studying python from apnacollege"
print(str.find("from"))

# counts the of  occurrer substr
str = "i am from studying python from apnacollege"
print(str.count("from"))


# conditional statements
age = 21
if(age >= 18):
    print("can vote & apply for license")
    print("can drive")

    # elif
light = "green"  
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
# else:
print("end of code")

# 
age = 24
if(age >= 18):
 if(age >= 80):
    print("can vote")
else:
    print("can not vote")


# next
marks = input("enter student marks")
if(marks >= 90):
    grade = 'A'
elif(marks + 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = " C"
else: grade = "D"
print(" grade of the student => ", grade)




