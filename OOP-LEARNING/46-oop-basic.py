# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex:- phone, cup, book
#          You need a "class" to create many objects
#          NOTE:- A method is a function that belongs to an object | Methods are the action that a object can perform

# class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)

# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)

car1.drive()
car2.drive()
car1.describe()
car2.describe()

        