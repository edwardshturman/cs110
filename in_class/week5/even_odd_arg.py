def even_or_odd(n):
    if (n % 2) == 0:
        print('This is an even number.')
    else:
        print('This is an odd number.')


def main():
    n = int(input('Enter a number: '))
    even_or_odd(n)


main()
