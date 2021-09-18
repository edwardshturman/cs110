n = int(input('Enter a number: '))

value = 1

for num in range(n, 1, -1):
    value *= num
print(str(n) + '! = ' + str(value))
