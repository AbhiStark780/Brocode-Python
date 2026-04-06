# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

# This is where we need the typecasting functions to convert the string into int or float as per our need

# name = input("Enter your name: ")
# age = int(input("enter your age: "))

# age = age + 1

# print(f"hello {name}!")
# print("HAPPY BIRTHDAY")
# print(f"you are {age} yours old.")

# EXERCISE 1 RECTANGLE AREA CALC

""" 
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print(f"The area is: {area}cm²") 

"""

# EXERCISE 2 Shopping Cart Program
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total bill is ${total}")