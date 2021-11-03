boy_names_file = open('BoyNames.txt', 'r')
boy_names = boy_names_file.readlines()
boy_names_file.close()

girl_names_file = open('GirlNames.txt', 'r')
girl_names = girl_names_file.readlines()
girl_names_file.close()

index = 0
while index < len(boy_names):
    boy_names[index] = boy_names[index].rstrip('\n')
    index += 1

index = 0
while index < len(girl_names):
    girl_names[index] = girl_names[index].rstrip('\n')
    index += 1

boy_name_search_query = input('Enter a boy\'s name, or N if you do not wish to enter a boy\'s name: ')
girl_name_search_query = input('Enter a girl\'s name, or N if you do not wish to enter a girl\'s name: ')

if boy_name_search_query == 'N':
    print('You chose not to enter a boy\'s name.')
else:
    search = boy_name_search_query in boy_names
    if not search:
        print(boy_name_search_query + ' is not one of the most popular boy\'s names.')
    else:
        print(boy_name_search_query + ' is one of the most popular boy\'s names.')

if girl_name_search_query == 'N':
    print('You chose not to enter a girl\'s name.')
else:
    search = girl_name_search_query in girl_names
    if not search:
        print(girl_name_search_query + ' is not one of the most popular girl\'s names.')
    else:
        print(girl_name_search_query + ' is one of the most popular girl\'s names.')
