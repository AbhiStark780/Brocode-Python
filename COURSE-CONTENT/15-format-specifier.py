# format specifier = {value:flags} format a value based on what 
#                             flags are inserted

# :.(number)f = round to that many decimal places (fixed point)
# :(number)f = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive number
# :, = comma seperator

price1 = 30000.14159
price2 = -98700.67
price3 = 34000.78

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")

# you can use a single flag or you can mix match multiple flags to get your desired result (no use of any separator between the multiple flags)