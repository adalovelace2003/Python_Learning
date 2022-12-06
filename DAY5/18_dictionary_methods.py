myDict = {
    "Fast": "In a Quick Manner",
    "Ada": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'},
    1: 2
}

# print(myDict.keys())  # prints all the keys of myDict
# print(type(myDict.keys()))  # prints the type
# 
# print(myDict.values())  # prints the values

# print(myDict.items()) # print key, value for all contents of dictionary

# print(myDict)
updateDict = {
    "Lovish" : "Friend",
    "Subham" : "Friend",
    "Divya" : "Friend"
}
myDict.update(updateDict)   #updates the dictionary by adding key-value pairs 
# from updateDict
# print(myDict)



# difference between .get and [] syntax 
print(myDict.get("Ada2"))   # Returns none if value is not present
print(myDict.get("Ada"))   # Returns none if value is not present
# print(myDict["ada2"])       #this will throw error as ada2 is not in dictionary

