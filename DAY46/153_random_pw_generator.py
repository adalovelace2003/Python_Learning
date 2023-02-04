import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90)) 
uppercaseLetter3=chr(random.randint(65,90)) 
uppercaseLetter4=chr(random.randint(65,90)) 
uppercaseLetter5=chr(random.randint(65,90)) 
uppercaseLetter6=chr(random.randint(65,90)) 

password1 = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 # + ....

uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90)) 
uppercaseLetter3=chr(random.randint(65,90)) 
uppercaseLetter4=chr(random.randint(65,90)) 
uppercaseLetter5=chr(random.randint(65,90)) 
uppercaseLetter6=chr(random.randint(65,90)) 

password2 = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 # + ....

password = password1 + password2

#Generate password using all the characters, in random order
password = shuffle(password)

#Ouput
print(password)
