girl_names_file = open('GirlNames.txt', 'r')
girl_names = girl_names_file.readlines()
girl_names_file.close()

names_searched_file = open('NamesSearched.txt', 'w')
names_searched = []

index = 0
while index < len(girl_names):
    girl_names[index] = girl_names[index].rstrip('\n')
    index += 1

girl_name_search_query = input('Enter a girl\'s name, or \'exit\' to stop searching: ')

while girl_name_search_query != 'exit':
    names_searched.append(girl_name_search_query)
    search = girl_name_search_query in girl_names
    if not search:
        print(girl_name_search_query + ' is not one of the most popular girl\'s names.')
    else:
        print(girl_name_search_query + ' is one of the most popular girl\'s names.')
    girl_name_search_query = input('Enter a girl\'s name, or \'exit\' to stop searching: ')

for name in names_searched:
    names_searched_file.write(str(name) + '\n')

names_searched_file.close()
