class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai): # salary after increment -> sai
        self.increment= sai/ self.salary
        

e= Employee()

print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 2000
    
print(e.salaryAfterIncrement)
print(e.increment)
