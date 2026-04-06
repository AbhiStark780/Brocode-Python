# iterables = An object/collections that can return its elements one at a time,
#             allowing it to be iterated over in a loop

# LIST, TUPLE, SET, STRING, DICTIONARY

# numbers = [1, 2, 3, 4, 5]
# numbers = (1,2,3,4,5)

# for number in (numbers):
#     print(number, end=" ")

# fruits = {"apple", "banana", "orange", "cocunut"}

# NOTE:- we cannot use reversed() function for set because set is a unordered collection of items

# for fruit in fruits:
#     print(fruit)

# name = "abhishek"

# for character in name:
#     print(character, end=" ")

my_dictionary = {"A": 1, "B": 2, "C": 3}

for key,value in my_dictionary.items():
    print(f"{key}:{value}")
