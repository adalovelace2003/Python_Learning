a = 54

def func1():
    global a        # writing global a will force the local variable to merge with global variable
                    # As a result global variable will be changed 
    a = 8           # local variable will not change the value of global variable
    print(a)
    

func1()
print(a)