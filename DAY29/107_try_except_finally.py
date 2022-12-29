#  If try doesnt throw error it will go to else ,if the condition goes to except else will not execute 
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit(0)
else:
    print("We were successful")

finally:    # this will even print if the program is even exited like above in except()
    print("We are done! ")