class Employee:
    company = "Camel"
    salary = 1000
    salarybonus = 100
    # totalSalary = 1100
    # instead of this hard coding  we will make the functin like  thing, but should work like property 
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus
    
    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus = val - self.salary
    
    
e = Employee()
print(e.totalSalary    )
e.totalSalary= 1200

print(e.salary)
print(e.salarybonus)

e.totalSalary= 2500

print(e.salary)
print(e.salarybonus)