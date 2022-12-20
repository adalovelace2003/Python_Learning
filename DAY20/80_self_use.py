class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")
        
harry = Employee()
harry.salary = 1000
harry.getSalary()
