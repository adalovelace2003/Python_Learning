story = "once upon a time there was a village."

# String Functions

#length 
print(len(story))   # length of characters

#check if the string ends with xyz
print(story.endswith("age.")) # will return true
print(story.endswith("haha")) # will return false

#string.count # count the number of character 
print(story.count("a")) 
print(story.count("Once"))

#capitalize    # capitalizes the first letter of the string
print(story.capitalize())

#find function  # gives the exact location where the word is ( gives index )
# only finds the first occurence 
print(story.find("upon"))

#replace
print(story.replace("upon", "upon_replaced"))

#Escape squence characters 
# \n 
# \t 
# \'
# \\ 