class Animal:
    animaltype = "Mammal"
    
class Pets(Animal):
    color = "white"
    
class Dog(Pets):
    
    @staticmethod
    def bark():
        print("Bow bow!")
        
d = Dog()

d.bark()