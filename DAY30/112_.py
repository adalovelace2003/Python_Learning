a = [3, 6, 7, 6, 8, 9, 2, 3, 9, 123, 67, 89]

# b = []
# for item in a :
#     if item% 2 == 0:
#         b.append(item)

# print(b)


# shortcut to write the same 
b = [i for i in a if i%2==0]
print(b)



