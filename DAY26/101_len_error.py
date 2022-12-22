class Vector:
    def __init__(self, vec):  # vec = list
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]  # returned after string slicing

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        # chekcing if both the vector have same dimension , if not print error message
        print("Multiply is happening!")
        print(len(self))
        print(len(vec2))
        
        if len(self) != len(vec2):
            print(" Two vector must have same dimensions to multiply")
            return
        else:
            for i in range(len(self.vec)):
                sum += self.vec[i] * vec2.vec[i]
            sum = 1
            return sum

    def __len__(self):
        return len(self.vec)
        
v1 = Vector([1, 4,3])
print(v1)

v2 = Vector([1, 2,3,4])
print(v2)

print(v1+v2)
print(v1*v2)

print(len(v1))
