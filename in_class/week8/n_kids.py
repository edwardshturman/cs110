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
