# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values baseed on a condition
#                          X if condition else Y

num = 7
a = 5
b = 6
age = 13
temperature = 30
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# result = "Even" if num % 2 == 0 else "ODD"
# print(result)

# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)