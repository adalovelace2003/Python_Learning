#  If try doesnt throw error it will go to else ,if the condition goes to except else will not execute 
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:  
    print(e)
else:
    print("We were successful")