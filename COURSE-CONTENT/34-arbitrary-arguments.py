# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional, 2. default, 3. keyword, 4. ARBITARARY


# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1,2,3, 6, 7, 8,9,0))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Mr.", "Abhishek", "the", "great", "tipiria") # here we are packing all these arguments in a tuple which we are going to use in the function

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="22 St.",
#               apt="100",
#               city="Baripada",
#               state="Odisha",
#               pincode="757001")


# EXERCISE [PRINT A SHIPPING LABEL]
def shipping_label(*args, **kwargs):     # the order of arguments will be this positonal argumets(*args) folled by keyword arguments(**kwargs)
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('pin')}")

shipping_label("Dr.", "Abhishek","Tipiria","II",
               street="22 St.",
               city="Baripada",
               state="Odisha",
               pin="757107")