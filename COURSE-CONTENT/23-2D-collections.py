# A collections within a collections

fruits =     ["apple", "orange", "banana", "coconut"]  # think of it as a matrix
vegetables = ["celery", "carrots", "potatoes"]          # you can access the elemets using the index [row][col] (just like coordinates)
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# print(groceries[0])

# print(groceries[0][0]) # to access the elements in 2D collections you need two indexes

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()


# EXERCISE make a 2D key pad that is found in phone

num_pad = ((1, 2, 3),
            (4, 5, 6), 
            (7, 8, 9), 
            ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()