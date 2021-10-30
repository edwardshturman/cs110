def print_menu():
    print('======================')
    print('Welcome to Dons Bank')
    print('What can I do for you?')
    print('1 - Withdraw Funds')
    print('2 - Deposit Funds')
    print('3 - Show Balance')
    print('4 - Quit')


def main():
    my_balance = 1000
    user_choice = 0

    try:
        while user_choice != 4:
            print_menu()
            user_choice = int(input('Please choose one of the above options: '))

            if user_choice == 1:
                again = True

                while again:
                    try:
                        amount = int(input('Amount to withdraw: '))
                        again = False
                    except ValueError:
                        print('Invalid amount, please enter an integer amount.')

                while my_balance - amount < 0:
                    print('Sorry: you don\'t have that much money in your account.')
                    again = True
                    while again:
                        try:
                            amount = int(input('Amount to withdraw: '))
                            again = False
                        except ValueError:
                            print('Invalid amount, please enter an integer amount.')

                my_balance = my_balance - amount
                print('New balance: ', my_balance)

            elif user_choice == 2:
                again = True
                while again:
                    try:
                        amount = int(input('Amount to deposit: '))
                        again = False
                    except ValueError:
                        print('Invalid amount, please enter an integer amount.')

                my_balance = my_balance + amount
                print('New balance: ', my_balance)

            elif user_choice == 3:
                print('Balance: ', my_balance)

            elif user_choice == 4:
                continue

            else:
                print('Invalid option. Please choose an option by entering 1, 2, 3, or 4.')

        print('Thank you. Goodbye!')

    except ValueError:
        print('Invalid option. Please choose an option by entering 1, 2, 3, or 4.')


main()
