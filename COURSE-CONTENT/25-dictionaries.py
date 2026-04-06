# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

# you can get the value associated with this key (you can use the get() method to check if a key is present in a dictionary or not)
# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")


# using update() method you can add new key:value pair or update existing key:value pair
# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Washington DC"})


# capitals.pop("China") # pop() removes a item from the dictionary
# capitals.popitem()  # popitem() will remove the latest key:value pair that was inserted
# capitals.clear()

# keys = capitals.keys()  # it returns a list so it is iterable

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)


# items() returns a 2D collection of Tuples in this form [(), (), () ...]
# items = capitals.items()  

# for key, value in capitals.items():
#     print(f"{key}: {value}")

# print(items)

