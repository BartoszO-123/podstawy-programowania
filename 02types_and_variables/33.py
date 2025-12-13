###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
celcius = float(input("Enter temperature in Celcius:"))
# Celcius to Kelvin
kelvin = celcius + 237.15
# Celcius to Fahrenheit
fahrenheit = celcius * 9 / 5 + 32
# Results
print(f"Temperature in Celcius: {celcius}")
print(f"Temperature in Kelvin: {kelvin}")
print(f"Temperature in Fahrenheit:{fahrenheit}")
