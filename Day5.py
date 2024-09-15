# # Loops in python
# # count = 1
# # while count <= 5 :
# #     print("hello")
# #     count += 1
# #     print("count")



# #  print number from 1 to 5
# i  = 1
# while i <=5:
#     print(i)
#     i +=1
#     print("loop ended")

# #  1 2 3 4 5 
#     # 



#     i  = 5
# while i >=1:
#     print(i)
#     i +=1
#     print("loop ended")
#     # 5 4 3 2 1


# Break and continue Loops in python

    # Break loop
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
    print("end of loop")


# Continue

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1


# Range()

seq = range(10)
for i in seq:
    print(i)

 #  
for i in range(10):
        print(i)

# Range ( start? , stop, step?)
for i in range(2, 10, 2):
     print(i)

# print even  numbers
for i in range(2,100,2):
     print(i)

