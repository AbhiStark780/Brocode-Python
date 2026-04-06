# string = sequence of characters

# print(help(str)) # This code will give details about string and its available methods in details


# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")

# result = len(name)  # len() this function returns the length of the string

# result = name.find(" ") # it returns the index in which the first occurence of the character is present

# result = name.rfind("a") # it returns the index of the last occurence of the character

# name = name.capitalize() # capitalize the first character of a string

# name = name.upper() # it makes all the characters of the string uppercase

# name = name.lower() # it makes all the charcters of the string lowercase

# result = name.isdigit() # it returns true/false if all the charcters in the string are digits or not

# result = name.isalpha() # returns boolean value if the string conatins onlt alphabets ot not

# result = phone_number.count("-")  # it returns the count of number of occurences of a charcter in the string

# phone_number = phone_number.replace("-", " ") # it replaces a certain charcter with another character in a string

# print(phone_number)

#------------------------------------------------------------------------------------------------------------

# EXERCISE 
# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contains digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")