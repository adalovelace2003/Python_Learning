class Employee:

    # Constructor
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee  is created!")

    def getName(self):
        print(f"Name is {self.name}")
    
    def getSalary(self):
        print("self.salary")
        

ram = Employee("Harry",100,"Printers")

ram.getName()