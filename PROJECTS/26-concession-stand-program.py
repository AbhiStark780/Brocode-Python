# Concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "samosa": 2.00,
        "popcorn": 6.75,
        "lemonade": 1.50,
        "fries": 2.50,
        "sprite": 2.99,
        "chips": 0.99}

cart = []
total = 0

print("----------MENU----------")
for key, value in menu.items():
    print(f"{key:>10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("------------YOUR ORDER------------")
for food in cart:
    total = total + menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")