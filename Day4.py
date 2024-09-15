# Dictionary and set
info = {
    "name" : "apnacollege",
    "subj" : ["python", "c", "java"],
    "topic" : ("dict", "set"),
    "age" : 34,
    "marks" : 94.2,
    12.99 :97.4
}
print(info["name"])
print(info["age"])

info["name"] = "pooja"
print(info)

#null dict

null_dict = {}
null_dict["name"] = "pooja"
print(null_dict)

#Nested Dictionaries

student ={
    "name" : "pooja",
    "score":{
        "chem" : 98,
        "phy": 97,
        "math": 96
    }
}


#dictionary methods
 

# myDict.keys() #return all key
print(len(list(student.keys())))


# myDictvalue() return all values
print(list(student.values()))


# myDict,item() return all key val pairs as tuples
print(list(student.items()))


# myDict.get("key") return thekey accoring to value
print(list(student.get()))


# myDicy.update(newDict) insert the specified items to the dictionary

new_dict = {"city": "delhi"}
student.update(new_dict)
print(student)

# set
collection = {1,2,3,4,5,6, "hello", "wolrd"}
print(collection)
print(type(collection))

collection = set() #empty set syntax
print(type(collection))


# Set Methods

# set.add(el)add an elememt

collection = set()
collection.add(1)
collection.add(2)
collection("pooja")
collection.add((1,2,3))
print(collection)

# set.remove(el) remove the elem an
collection.remove(1)

# set clear () empties the set
collection.clear()

# set.pop() removes a random value
collection = {"hello", "pooja", "rawat"}
print(collection.pop())

# set.union (set2) combines both set values and returns new

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1)
print(set2)

# set.inersection(set2) combines common values and return new

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.intersection(set2))

