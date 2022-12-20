''' 
1 2 3 4 5 6 7 8 9 10
'''


class Train:

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"THe name of the train is {self.name} ")
        print(f"THe seats of the train is {self.seats} ")

    def fareInfo(self):
        print(f"The fare is Rs. {self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(
                f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try later")

    def cancelTicket(self):
        self.seats = self.seats + 1
        print("The seat has been cancelled")


print("\n\n\n")
intercity = Train("Intercity", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()

intercity.cancelTicket()
intercity.bookTicket()

intercity.cancelTicket()

intercity.bookTicket()
# intercity.bookTicket()    # kindly try later
intercity.getStatus()

print("\n\n\n")
