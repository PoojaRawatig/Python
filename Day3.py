# list og tuple in python

marks = [84.3, 34, 56, 67, 56, 67, 67.8 , 45]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])


#list slicing
marks = [84.3, 34, 56, 67, 56, 67, 67.8 , 45]
print(marks[1:4])


# list methods
list = [2,1,3]

# 
list.append(4) #Add one element at the end [2,1,3,4]
list = [2,1,3]
list.append(4)
print(list)

# 
list.sort() #sort in ascending order [1,2,3]
list = [2,1,3]
print(list.sort())
print(list)

# 
list.sort(reverse=True) #sorts in descending order  [3,2,1]

list = ["banana", "apple", "litchi"]
print(list.sort(reverse=True))
print(list)



# 
list.reverse() # reverse list  [3,1,2]

list = ["banana", "apple", "litchi"]
list.reverse()
print(list)


# 
# list.insert(index.element) #inset element at index
list = [2,1,3]
list.insert(1,5)
print(list)


#remove
list = [2,1,3]
list.pop(2)
print(list)

# tuple
tup = (2,1,3,1)
print(tup[0])
print(tup[1])

tup = (1,2,3,4,5)
print(tup.count(2))