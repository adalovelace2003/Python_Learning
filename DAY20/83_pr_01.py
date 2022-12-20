class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product
    # print("Created Successfully!")

    def getInfo(self):
        print(
            f" \n\nTHe name of the {self.company} programmer is {self.name} \nand the product is {self.product}\n\n")


harry = Programmer("Harry", "Skype")

harry.getInfo()



ada = Programmer("Ada", "Github")

ada.getInfo()
