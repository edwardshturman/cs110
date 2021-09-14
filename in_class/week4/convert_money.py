# Write a program (convert_money.py) that prompts the user like this:
# Currency to convert to U.S. dollars:
# e = Euros, c = Chinese Yuan, r = Indian Rupees, b = Bitcoin:
# Then depending on which letter the user enters, the program displays:
# 'Amount of Euros/Yuan/Rupees/Bitcoin to convert: '
# (Note: the second prompt should only name the one currency the user asked to convert, not all four currencies.)
# After the user enters the amount, the program displays the amount converted to U.S. dollars to 2 decimal places;
# e.g. 'In U.S. dollars, that is $24.83'
#
# Conversion rates (from Google, Aug 6, 2018):
# 1 Euro = 1.16 US dollar
# 1 Chinese Yuan = 0.15 US dollar
# 1 Indian Rupee = 0.015 US dollar
# 1 Bitcoin = 6923.80 US dollar


currency_to_convert = input('Currency to convert to U.S. dollars:\n\'e\' = Euros\n\'c\' = Chinese Yuan\n\'r\' = '
                            'Indian Rupees\n\'b\' = Bitcoin\n\n')
if currency_to_convert == 'e':
    euro_convert = float(input('Amount of Euros to convert: '))
    print('In U.S. dollars, that is $' + format(euro_convert * 1.16, '.2f') + '.')
elif currency_to_convert == 'c':
    yuan_convert = float(input('Amount of Yuan to convert: '))
    print('In U.S. dollars, that is $' + format(yuan_convert * 0.15, '.2f') + '.')
elif currency_to_convert == 'r':
    rupee_convert = float(input('Amount of Rupees to convert: '))
    print('In U.S. dollars, that is $' + format(rupee_convert * 0.015, '.2f') + '.')
elif currency_to_convert == 'b':
    bitcoin_convert = float(input('Amount of Bitcoin to convert: '))
    print('In U.S. dollars, that is $' + format(bitcoin_convert * 6923.80, '.2f') + '.')
else:
    print('You need to enter either \'e\', \'c\', \'r\', or \'b\'!')
