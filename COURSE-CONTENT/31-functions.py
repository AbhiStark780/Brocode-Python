# function = A block of reusable code
#            place() after the function name to invoke it

# return = statement used to end a function
#          and send a result back to the caller


# def happy_birthday(name, age):                # this is the function defination with some parameters
#     print(f"Happy Birthday to you {name}")        # parameter is like a temporary variable that is used within a function
#     print(f"You are {age} years old")                 # the postions of parameters matters

# happy_birthday("Abhishek", 20) # this is where we called the function by giving some arguments
# happy_birthday("steve", 30)           # any data/variable you send to a function are called arguments
# happy_birthday("dodo", 40)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Abhishek", 49.79, "13th march")


# def add(x, y):
#     z = x + y
#     return z

# def sub(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def division(x, y):
#     z = x / y
#     return z


# z = add(1, 2)

# print(z)
# print(sub(10, 5))
# print(division(10, 60))

# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last         # using the return we can return some data back to the place in which you call a function

# full_name = create_name("abhishek", "tipiria")

# print(full_name)