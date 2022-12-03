first_name = "Ada"
last_name = "Lovelace"
print(type(first_name))  # prints the data type of name

print(first_name+"\t"+last_name)    # concatenation

full_name = first_name+last_name    
print(full_name)

'''
Ada Lovela 
0123456789
''' 
#counting starts from 0 in programming 
print(first_name[0]) # print the first letter of the string by 0

# You can't change the some letter of the string like
# first_name[2]="Z" # error str object doesnt support item assignment

print(full_name[0:5])   # this will print 0 - 4 character like for this AdaLo
print(full_name[:5])   # this will print 0 to 5 
print(full_name[0:])   # this will print all afer 0 index

# Negative Index
#  if you dont know the full length of string and want to print the last letter 
# then use -1 as index

print(full_name[-1])

# Slicing with skip value

#  full_name[ 0 : 5 : 2 ] skips 1 character 
#  full_name[ 0 : 5 : 1] skips nothing

print(full_name[0: :2])
