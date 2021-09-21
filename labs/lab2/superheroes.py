#  Set initial values
choice = 1
wonder_woman_total = 0
thor_total = 0
batwoman_total = 0
superman_total = 0

#  Print main menu
print('\nWelcome to the CS 110 Action Figure Shop!')
while 1 <= choice <= 4:
    print('Which action figure would you like to collect?\n')
    print('1. Wonder Woman')
    print('2. Thor')
    print('3. Batwoman')
    print('4. Superman')
    print('5. Exit\n')

    choice = int(input('Please enter your choice (1-5): '))

    #  Input validation
    while choice < 1 or choice > 5:
        print('\nThat\'s not a valid choice!\n')
        print('1. Wonder Woman')
        print('2. Thor')
        print('3. Batwoman')
        print('4. Superman')
        print('5. Exit\n')
        choice = int(input('Please reselect: '))

    #  Wonder Woman submenu
    if choice == 1:
        wonder_woman_total += int(input('How many Wonder Woman action figures would you like to collect? '))

    # Thor submenu
    if choice == 2:
        thor_total += int(input('How many Thor action figures would you like to collect? '))

    # Batwoman submenu
    if choice == 3:
        batwoman_total += int(input('How many Batwoman action figures would you like to collect? '))

    # Superman submenu
    if choice == 4:
        superman_total += int(input('How many Superman action figures would you like to collect? '))

    # Exit option
    if choice == 5:
        print('\nThanks for visiting the CS 110 Action Figures Shop! You collected:\n')
        print('Wonder Woman: ' + str(wonder_woman_total))
        print('Thor: ' + str(thor_total))
        print('Batwoman: ' + str(batwoman_total))
        print('Superman: ' + str(superman_total))
        print('\nCome again soon!\n')
