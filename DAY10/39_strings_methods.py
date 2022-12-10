#  Strings are Immuatble

a = "Harry!!!!!!"
A = "h arry"
aa = "Harry !!!!!! HARRY "
aaa="introduction to Python"
b= " He's name is John. He is an honest man"
c= "I have 200,00 $ of cash in my bank"
print(len(a))

print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))

print(aa.split(" "))

print(aaa.capitalize()) # Capitalizes first letter 

print(aaa)
print(aaa.center(40))

print(aaa.count("Python"))

print(aaa.endswith("on"))

print(b.find("is"))

print(b.index("is")) #gives error

print(c)

print(b.isalnum())
print(A.isalnum())

print(A.isalpha())
print(c.isalpha())

print(c.islower())
print(A.islower())



