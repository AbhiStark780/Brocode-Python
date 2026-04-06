# while loop = execute some code WHILE some condition remains true

# this is mainly used for validating user input (prompting the user for input until it satisfies the required input condition/format)

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter yor name")
#     name = input("Enter your name: ")

# print(f"Hello, {name}")

# ---------------------------------------

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"Your are {age} years old.")

# ----------------------------------------

# food = input("Enter a food you like: ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like (q to quit): ")

# print("bye")

# ------------------------------------------

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")


