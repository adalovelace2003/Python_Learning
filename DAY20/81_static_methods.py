class Employee:
    company = "Google"

    def getSalary(self):
        print(f"Salary is {self.salary}")


    def getSalaryNsign(self,signature):
        print(f"Salary is {self.salary} {signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")


# harry.getSalary()    # Employee.getSalary(harry)
''' Adding @static method will stop the need of self making the code work like this Employee.greet(harry)        '''


harry = Employee()
harry.salary = 1000

harry.greet()


harry.getSalaryNsign("\nThanks")
