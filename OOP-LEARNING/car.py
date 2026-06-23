

class Car:
    def __init__(self, model, year, color, for_sale): # below variables are called instance variable 
        self.model = model                            # they are defined inside the constructor
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")