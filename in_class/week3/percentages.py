# Write a program percentages.py that asks the user for the number of CS majors and the number of non-CS majors
# registered in a class. The program should display the percentage of CS majors and non-CS majors in the class to 2
# decimal places along with the % sign with no space.
#
# Hint: Suppose there are 8 CS majors and 12 non-CS majors in a class. There are 20 students in the class. The
# percentage of CS majors can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage of non-CS majors can be
# calculated as 12 ÷ 20 = 0.6, or 60%.


cs_majors = int(input('How many CS majors are in the class? '))
non_cs_majors = int(input('How many non-CS majors are in the class? '))

total_students = cs_majors + non_cs_majors

cs_majors_percentage = cs_majors / total_students * 100
non_cs_majors_percentage = non_cs_majors / total_students * 100

print(format(cs_majors_percentage, '.2f') + '% of the class is composed of CS majors, while ' + format(non_cs_majors_percentage, '.2f') + '% of students in the class are not CS majors.')
