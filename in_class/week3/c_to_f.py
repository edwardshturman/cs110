# Write a Python program c_to_f.py that converts a given temperature in Celsius to Fahrenheit.
# Steps for the algorithm are:
# Input the temperature in Celsius
# Output Fahrenheit to 2 decimal places in this format:
# 'Temperature in Fahrenheit is: ' and the temp in F using this formula:
# F = (9/5) * Celsius + 32


temp_celsius = float(input('What is the temperature in Celsius? '))
temp_fahrenheit = (9 / 5) * temp_celsius + 32
print('Temperature in Fahrenheit is: ' + format(temp_fahrenheit, '.2f') + '°F')
