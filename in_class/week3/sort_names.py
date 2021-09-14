# Write a Python program sort_names.py where the user enters two names and you print them in sorted order,
# lowest to highest (lowest means the word with the lowest ASCII code value, e.g., Mark < Mary),
# i.e. in alphabetical order. You should print it in the format: firstname, secondname.


first_name = input('First name: ')
second_name = input('Second name: ')
if first_name > second_name:
    print(first_name, second_name)
elif second_name > first_name:
    print(second_name, first_name)
else:
    print('Error in calculation.')
