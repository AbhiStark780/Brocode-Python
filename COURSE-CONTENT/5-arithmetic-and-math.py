import math


# Arithmetic operators:- +  -  *  /  **  %

# Augumented assignment:- +=  -=  /=  **=  %=

x = 3.14
y = 4
z = 5

# result = round(x)  return the rounoff of a number
# result = abs(y)    return the absolute value 
# result = pow(5, 3)   return  5  to the power of 3 (i.e 5*5*5)
# result = max(x, y, z)  return the maximum number from the given set of numbers
# result = min(x, y, z)  return the minimum number from the given set of numbers

f = 9.1

# print(math.pi)
# print(math.e)
# result = math.sqrt(9)
# result = math.ceil(f)   returns the closest integer greater than the given number
# result = math.floor(f)  returns the closest minimum integer than the given number


# EXERCISE 1: CALULATE THE CIRCUMFERENCE OF A CIRCLE [Formula:- 2 * pie * radius]
# radius = float(input("Enter the radius of the circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)} units")

#--------------------------------------------------------------------------------

# EXERCISE 2: CALCULATE THE AREA OF A CIRCLE [Formula: pie * radius * radius]

# radius = float(input("Enter the radius of the circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of circle is: {round(area, 2)} units")

#----------------------------------------------------------------------------------

# EXERCISE 3: FIND THE HYPOTENOUS OF A RIGHT ANGLED TRIANGLE

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")

