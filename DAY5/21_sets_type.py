# Creating an empty set
b = set()
print(type(b))


# Adding value to empty sets
b.add(4)
b.add(5)
b.add(6)
b.add(6)  # if i add the same value again , it only keeps one because
# set is the collection of non repetitive items
# b.add([1,2,3])      # throws error, unhashabel list
b.add((1, 2, 3))      # we can add tuple to the sets
b.add((1, 2, 3))      # we can add tuple to the sets
# b.add({4:5})  # you cannot add dictionary to the sets


print(b)

print(len(b))  # prints the length of b

b.remove(5)
print(b)


# b.remove(15)  # throws error if you try removing thats not in set

print(b.pop())
