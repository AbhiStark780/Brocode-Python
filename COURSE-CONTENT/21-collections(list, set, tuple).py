# collections = single "variable" used to store multiple values (each value in a collection is called an element)
#
# List  = [] ordered and changeable. Duplicates OK
#         you can use the index operator as of like you use in string(slicing, steps, etc)

# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates

# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# general naming convention is give your collection plural form as they contains multiple elements
# when using for loop to access the elements you can use the counter variable in singular form of the collection name (just a naming convention)


# ------------------LIST----------------------------------------

# fruits = ["apple", "orange", "mangoes", "coconut", "banana"] # general naming convention is give your collection plural form as they contains multiple elements

# print(fruits[::-1])

# for fruit in fruits:
#     print(fruit)

# print(dir(fruits))  # dir() displays all the attribute and methods we can use in list 
# print(help(fruits)) # help() displays all the details info about methods and attribute avilable

# print(len(fruits))

# print("apple" in fruits) # using the 'in' operator we can find if a element is present is a collection or not

# fruits[1] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("coconut"))
# print(fruits.count("banana"))

# print(fruits)

#-----------------------SET--------------------
# fruits = {"apple", "orange", "banana", "litchi"}
# print(dir(fruits))
# print(help(fruits))

# print(len(fruits))
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()

#----------------TUPLE-----------------
fruits = ("apple", "banana", "cocunut")

# print(len(fruits))
# print("apple" in fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))


print(fruits)