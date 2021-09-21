num = 0
minimum_value = 0
maximum_value = 0

while num != -1:
    num = int(input('Enter a number: '))
    if num == -1:
        print(minimum_value)
        print(maximum_value)
    elif num > maximum_value:
        maximum_value = num
    elif num < minimum_value:
        minimum_value = num
