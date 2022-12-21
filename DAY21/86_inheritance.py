class Employee:
    def __init__(self,name,group,age):
        self.name = name
        self.group = group
        self.age = age
    def getInfo(self):
        print(f"Name is : {self.name} , Age is {self.age}, Group is {self.group}")

class programmer(Employee):
        pass



ram = programmer("ram", "programmer", 10)
shyam = Employee("ram", "programmer", 10)


shyam.getInfo()

ram.getInfo()


#  Single inheritance to only one child 

#  Multiple parent one child is  multiple inheritance 

# 