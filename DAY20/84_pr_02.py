class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num **2} ")

    def cube(self):
        print(f"The cube of {self.num} is {self.num **3} ")


    def sqrt(self):
        print(f"The square of {self.num} is {self.num **0.5} ")


a = Calculator(5)

a.square()
a.sqrt()
a.cube()
