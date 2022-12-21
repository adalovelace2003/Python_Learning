class Person:
    country = "India"
    city = " Banglore"
    
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def takeBreak(self):
        print("I m breathing ...")

class Employee(Person):
    company= "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print("I m employee, I m breathing ...")
        
        
class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print("No salary to programmers")
        
    def takeBreak(self):
        print("I m employee, I m breathing ++")


ram = Person("ram", 10, 1000)
sita = Employee("sita", 20, 2000)
nana = Programmer("nana", 50, 9000)

ram.takeBreak()
sita.takeBreak()

nana.takeBreak()
