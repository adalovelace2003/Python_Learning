try:
    a = int(input("\n Enter a number : "))
    c = 1 / a
    print(c)
# except Exception as e:
    # print("Exception  0 occured")
    # print(e)

except ValueError as e:
    # print("Exception 1  occured")
    print("\n Please enter a valid value")
    # print(e)

except ZeroDivisionError as e:
    # print("Exception 2 occured")
    print("\n Make sure you are not divifing by zero")
    # print(e)
except :
    print("Unknown Error Occured")

print("\n Thanks for using this code! ")
