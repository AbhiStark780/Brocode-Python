# Temperature conversion program

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperarure: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"Temperarure in Fahrenheit is: {temp}°F") # [alt + 0176] for the degree symbol   
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"Temperarure in Celsius is: {temp}°C") 
else:
    print(f"{unit} is an invalid unit of measurement")