a = int(input('Enter an integer for the lower limit: '))
b = int(input('Enter an integer for the upper limit: '))

if a >= b:
    print('Error: ' + str(a) + ' > ' + str(b))

elif a < b:

    total = 0

    for n in range(a, b + 1, 1):
        total += n
    print(total)
