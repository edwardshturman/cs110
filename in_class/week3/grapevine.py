# A vineyard owner is planting several new rows of grapevines, and needs to know how many grapevines to plant in each
# row. She has determined that after measuring the length of a future row, she can use the following formula to
# calculate the number of vines that will fit in the row, along with the trellis end-post assemblies that will need
# to be constructed at each end of the row:
#
# V = (R - 2E) / S
#
# The terms in the formula are:
#
# V is the number of grapevines that will fit in the row.
# R is the length of the row, in feet.
# E is the amount of space, in feet, used by an end-post assembly.
# S is the space between vines, in feet.
#
# Write a program grapevine.py that makes the calculation for the vineyard owner. The program should ask the user to
# input the following: The length of the row, in feet. The amount of space used by an end-post assembly, in feet. The
# amount of space between the vines, in feet.
#
# Once the input data has been entered, the program should calculate and display the number of grapevines that will
# fit in the row to 2 decimal places.
#
# Hint: you will want to think about what data type your user's input will be.
#
# For example, your program would look like this with the following values:
# Enter the length of the row, in feet: 50
# Enter the amount of space, in feet, used by an end-post assembly: 0.5
# Enter the distance, in feet, between each vine: 12.2
# You have enough space for 4.02 vines.


row_length = float(input('What is the length of the row, in feet? '))
end_post_space = float(input('What is the amount of space used by an end-post assembly, in feet? '))
vine_room = float(input('What is the amount of space between the vines, in feet? '))

grapevines = format(row_length - (2 * end_post_space) / vine_room, '.2f')
print('The number of grapevines that will fit in a row:', grapevines)
