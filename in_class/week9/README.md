# Week 9

*October 19, 2021 – October 25, 2021*

## In-Class Exercise 9

### Part 1: Number of Kids

1. Grab the file `n_kids.txt` that contains data from the class on the number of kids your parents have (you + your siblings), one number per line.
2. Write a program `n_kids.py` that reads the data from `n_kids.txt`, does some math, then displays the following:
    - Total number of families
    - Total number of kids
    - Average number of kids per family (to 2 decimal places)
    - Maximum number of kids in a family
    - Minimum number of kids in a family
3. Extra credit: write the above results to a different file (`results.txt`, not to the input file `n_kids.txt`) in addition to displaying them on the screen.

Do not use built in `min` and `max` or similar functions.

```python
# Get n_kids.txt file
read_file = open('n_kids.txt', 'r')

# Set initial values
families = 0
kids = 0
smallest_number_of_kids = 10  # This value counts down, so purposely set high
largest_number_of_kids = 0

# Read first line to start while loop
line = read_file.readline()

# For each non-blank line, add one to families, add value of line to total kids count, and compare min and max kids
while line != '':
    line = line.lstrip('\ufeff')
    line = line.rstrip('\n')
    families += 1
    kids += int(line)
    if int(line) > largest_number_of_kids:
        largest_number_of_kids = int(line)
    if int(line) < smallest_number_of_kids:
        smallest_number_of_kids = int(line)
    line = read_file.readline()

read_file.close()

# Calculate average number of kids per family
avg_kids = format(kids / families, '.2f')

# Print values
print('Total number of families: ' + str(families))
print('Total number of kids: ' + str(kids))
print('Average number of kids per family: ' + str(avg_kids))
print('Maximum number of kids in a family: ' + str(largest_number_of_kids))
print('Minimum number of kids in a family: ' + str(smallest_number_of_kids))

# Write values to results.txt
write_file = open('results.txt', 'w')
write_file.write('Total number of families: ' + str(families) + '\n')
write_file.write('Total number of kids: ' + str(kids) + '\n')
write_file.write('Average number of kids per family: ' + str(avg_kids) + '\n')
write_file.write('Maximum number of kids in a family: ' + str(largest_number_of_kids) + '\n')
write_file.write('Minimum number of kids in a family: ' + str(smallest_number_of_kids) + '\n')
write_file.close()
```

![part1.png](assets/e9-part1.png)

### Part 2: Random Number File Writer

Write a program `rand_num.py` that writes a series of random numbers to a file `rand_num.txt`, one number per line. Each random number should be in the range of 1 through 500. The application should ask the user how many random numbers the file will hold with, "How many random numbers would you like?"

```python
import random

write_file = open('rand_num.txt', 'w')

lines = int(input('How many random numbers would you like? '))

for line in range(lines):
    number = random.randint(1, 500)
    write_file.write(str(number) + '\n')

write_file.close()
```

![part2.png](assets/e9-part2.png)

## In-Class Exercise 10

### ATM Program

- Start with the pre-written `bank_atm.py`.
- Test it to see how it works, and what makes it crash.
- Add exception-handlers so it doesn't crash when the user enters an invalid ATM option (**input that isn't an integer**) e.g. `a`.
    - If it’s invalid, e.g. `a`, you want a statement that says, "Invalid option. Please choose an option by entering 1, 2, 3, or 4." **Don't display the menu again.**
- Add exception-handlers to the withdrawal and deposit code, so the program doesn't crash on invalid money amount (**input that is not an integer**). **You don't want to take the user back to the main menu once they have already selected their option if they have an invalid input.**
    - If it's an invalid option you want to say, "Invalid amount, please enter an integer amount."
- If you are trying to make a withdrawal and enter an amount that would take you over the limit, and *then* enter an invalid input, make sure you have a check for that when you try again.

Original `bank_atm.py`:

```python
def printmenu():
    print("======================")
    print("Welcome to Dons Bank")
    print("What can I do for you?")
    print("1 - Withdraw Funds")
    print("2 - Deposit Funds")
    print("3 - Show Balance")
    print("4 - Quit")

def main():
    myBalance = 1000
    userChoice = 0
    while userChoice !=4:
        printmenu()
        userChoice = int(input("Please choose one of the above options: "))
        if userChoice == 1:
            amount = int(input("Amount to withdraw: "))
            while myBalance - amount < 0:
                print("Sorry: you don't have that much money in your account.")
                amount = int(input("Amount to withdraw: "))
            myBalance = myBalance - amount
            print("New balance: ", myBalance)
        elif userChoice == 2:
            amount = int(input("Amount to deposit: "))
            myBalance = myBalance + amount
            print("New balance: ", myBalance)
        elif userChoice == 3:
            print("Balance: ", myBalance)
        elif userChoice == 4:
            continue
        else:
            print("Invalid option.  Please choose an option by entering 1, 2, 3, or 4.")
    print("Thank you. Goodbye!")

main()
```

Updated version:

```python
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
```
