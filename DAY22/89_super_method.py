class Person:
    country = "India"
    city = " Banglore"
    
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        print("Initializing Person .. \n")
    
    def takeBreath(self):
        print("I m breathing ...")

class Employee(Person):
    
        
    company= "Honda"
    def __init__(self,name,age,salary):
        super().__init__(name,age,salary)
        print("Initializing Employee..\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I m employee, I m breathing ...")
        
        
class Programmer(Employee):
    company = "Fiverr"

    def __init__(self,name,age,salary):
        super().__init__(name,age,salary)
        print("Initializing Employee..\n")

    def getSalary(self):
        print("No salary to programmers")
         
    def takeBreath(self):
        super().takeBreath()
        print("I m programmer, I m breathing ++")


ram = Person("ram", 10, 1000)
sita = Employee("sita", 20, 2000)
nana = Programmer("nana", 50, 9000)

ram.takeBreath()
sita.takeBreath()
nana.takeBreath()
