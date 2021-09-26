def add(num1, num2):
    result = num1 + num2
    print(str(num1) + ' + ' + str(num2) + ' = ' + str(result))


def subtract(num1, num2):
    result = num1 - num2
    print(str(num1) + ' - ' + str(num2) + ' = ' + str(result))


def multiply(num1, num2):
    result = num1 * num2
    print(str(num1) + ' * ' + str(num2) + ' = ' + str(result))


def divide(num1, num2):
    result = num1 / num2
    print(str(num1) + ' / ' + str(num2) + ' = ' + str(result))


def main():
    go_back = 'y'
    while go_back == 'y' or go_back == 'Y':
        print('Welcome to the Calculator Program!')
        num1 = int(input('Enter your first number: '))
        num2 = int(input('Enter your second number: '))

        print('Please enter one of the following mathematical operators:\n')
        operator = input('+ (Addition)\n- (Subtraction)\n* (Multiplication) \n/ (Division)\n\n')

        while operator != '+' and operator != '-' and operator != '*' and operator != '/':
            operator = input('That\'s not a valid operator! Please reselect: ')

        if operator == '+':
            add(num1, num2)
            go_back = input('Would you like to go back? (Enter \'y\' or \'Y\'.) ')

        if operator == '-':
            subtract(num1, num2)
            go_back = input('Would you like to go back? (Enter \'y\' or \'Y\'.) ')

        if operator == '*':
            multiply(num1, num2)
            go_back = input('Would you like to go back? (Enter \'y\' or \'Y\'.) ')

        if operator == '/':
            divide(num1, num2)
            go_back = input('Would you like to go back? (Enter \'y\' or \'Y\'.) ')


main()
