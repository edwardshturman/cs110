import random

write_file = open('rand_num.txt', 'w')

lines = int(input('How many random numbers would you like? '))

for line in range(lines):
    number = random.randint(1, 500)
    write_file.write(str(number) + '\n')

write_file.close()
