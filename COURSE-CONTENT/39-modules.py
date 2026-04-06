# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program into seperate files

# print(help("modules")) # this gives a list of all the available modules
# print(help("math")) # use this to get the details of a specific module

# import math    # this imports the whole module
# import math as m  # gives an alias for the module name
# from math import pi # used to import a specific function or data from a module 
#                       [avoid using this as it can result in naming conflict with the local variables]


import example

result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)


print(result)
