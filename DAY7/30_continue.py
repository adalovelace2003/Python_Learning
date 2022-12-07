

for i in range(1,10):
    if i == 5:
        continue;  # continue will skip the condition and increase the loop value
                   # and goto next value 
    print(i)
else:       # else will run if the loop has gone through natural termination.
    print("This is inside else of for")
    