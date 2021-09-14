# Write a program water.py that asks for temperature in Fahrenheit.
# The program should accept any floating point number.
# Display whether water is liquid, solid, or gas at that temperature at sea level.
# Display the results like this: 'Water at that temperature is a solid/liquid/gas.'
# (Note: display only the correct state for that temperature.)
#
# Facts: At sea level, water freezes at 32 degrees F and boils at 212 degrees F.
#
# Extra credit: 1 point if you convert the temperatures to celsius when printing.


temperature_f = int(input('What is the temperature? '))
temperature_c = int((temperature_f - 32) * 5/9)
if temperature_f <= 32:
    print('Water at temperature ' + str(temperature_c) + '°C is a solid, as it has frozen.')
elif temperature_f >= 212:
    print('Water at temperature ' + str(temperature_c) + '°C is a gas, as it has evaporated.')
else:
    print('Water at temperature ' + str(temperature_c) + '°C is a liquid, as it has neither frozen nor evaporated.')
