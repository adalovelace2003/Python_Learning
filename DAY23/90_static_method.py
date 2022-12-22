class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"
    
    # def changeSalary(self,sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal
    
    
    
    
    
e = Employee()
print(Employee.salary)
print(e.salary)

e.changeSalary(455)

print(e.salary)
print(Employee.salary)


```
Day 23 || Python ||
#Day23 #mrslovelace01 #day_23_of_learning_python #askbuddie
Day 23 || Dec 23 || 10:15
Things that I learned & did today:
1. Getter 
2. Setter 
Reference: || CodeWithHarry ||
Github: https://github.com/adalovelace2003/Python_Learning
#day_23_of_learning_python_askbuddie #codingchallenge #ask_buddie #coding_challenge
```