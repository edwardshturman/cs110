# Write a Python program sale_price.py that does the following:
# Gets in the original price of an item as input.
# Calculates the discounted price with a 40% discount.
# Prints the sale prices as output in the correct format (ex: $2.45).


original_price = float(input('What is the original price? '))
discounted_price = original_price * (60 / 100)
print('The discounted price is: $' + str(discounted_price))
