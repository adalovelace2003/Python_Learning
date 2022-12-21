class Employee:
    company = "Visa"
    ecode = 120

class Freelancer:
    company = "Fiverr"
    level =2
    
    def upgradeLevel(self):
        self.level += 1

class Programmer(Employee, Freelancer):
    name = "Rohit"
    # company= "self"

ram = Programmer()
print(ram.level)
ram.upgradeLevel()
print(ram.level)

print(ram.company)


 