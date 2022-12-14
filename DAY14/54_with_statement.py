

#  You dont have to close the file after opening with "with statement"


with open('another.txt','r') as f:
    a = f.read()
print(a)


with open('another2.txt','w') as f:
    a = f.write("me")
print(a)