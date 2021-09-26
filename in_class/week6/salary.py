def constant_salary():
    rate = 100
    days = 10
    total = rate * days
    return total


def doubling_salary():
    total = 1
    for num in range(1, 10, 1):
        # Note: normally, range would end at 11, but having total set to 1 is day 1, so run range for 9 more days
        total *= 2
    return total


def main():
    constant_salary_total = constant_salary()
    doubling_salary_total = doubling_salary()
    print('The total income for Option 1 is: $' + str(constant_salary_total))
    print('The total income for Option 2 is: $' + str(doubling_salary_total))
    print('The salary option with the most income is Option 1.')


main()
