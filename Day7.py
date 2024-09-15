# file i/o in python

#types of all files

# 1. Text Files: txt, docx, log, etc
# 2.Binary File. mp4, mov, png, jpeg,

f = open("demo.txt", "r")
data = f.read(5)
print(data)
print(type(data))
f.close()

# Reading a file
data = f.read() #reads entire file
data = f.readline()  #reads one line at a time


line1 = f.readline()
print(line1)
f.close()


# write
f = open("demo.txt", "w")
f.write("i want to learn javascript tomorrow.123")
f.close()

# append
f = open("demo.txt", "a")
f.write("i want to learn javascript tomorrow.123")
f.close()


# create file
f = open("sample.txt", "a")
f.close()

# file override
f = open("demo.txt", "r+")
f.write("abc")
f.close()

#
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

# deleting a file
import os
os.remove("sample.txt")