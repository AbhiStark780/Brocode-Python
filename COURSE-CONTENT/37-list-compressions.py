# List comprehension = A consise way to create lists in python 
#                      Compact and easier to read then traditional loops
#                      [expression for value in iterable if condition]


# doubles = []
# for x in range(1, 11):
#     doubles.append(x*2)

# print(doubles)

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]

# print(doubles)
# print(triples)
# print(squares)

# fruits = ["banana", "apple", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]

# print(fruits)

# numbers = [1, -2, 3, -4, 5, -6]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]

# print(positive_nums)
# print(negative_nums)

grades = [85, 42, 79, 56, 61, 78]

passing_grades = [grade for grade in grades if grade >=60]

print(passing_grades)