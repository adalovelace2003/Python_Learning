#  If try doesnt throw error it will go to else ,if the condition goes to except else will not execute 
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
else:
    print("We were successful")

finally:    # this will even print if the program is even exited like above in except()  
    # Finally executes regardless of error 
    print("We are done! ")
    
 