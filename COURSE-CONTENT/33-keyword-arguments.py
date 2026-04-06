# keyword arguments = an argument preceded by an identifier
#                     helps with readibility                     
#                     order of arguments doesn't matter
#                     1. positional, 2. default, 3. KEYWORDS, 4. arbitary


# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# hello(greeting="Good Morning", first="Abhishek",title="Mr.",last="Tipiria")

# for x in range(1,11):
#     print(x,end=" ")

# print("1","2","3","4","5",sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=+91,area=123,first=456,last=789)
print(phone_num)