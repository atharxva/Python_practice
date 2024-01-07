class Car:
    def __init__(self):
        pass
    def input(self):
        self.model = input("Enter the number")
        self.year   = input("Enter the year of make")
        self.name = input("Enter the price")
    def display(self):
        print("The model number is :",self.model)
        print("The year is :",self.year)
        print("The name is :",self.name)

obj = self.Car
obj.display()