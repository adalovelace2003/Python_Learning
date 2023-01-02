#  write mul table to the file using compherension list
num = int(input("Enter your number : "))

table = [num*i for i in range(1, 11)]
print(table)
i = 1
with open(f"table_of_{num}.py","a") as f:
    for value in table:
        f.write(f"#{i}.\t{num} X {i} = {value}\n")
        i+=1
        
