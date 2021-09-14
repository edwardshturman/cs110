# Get date input from user
year = int(input('Input a year: '))
month = int(input('Input a month [1-12]: '))
day = int(input('Input a day [1-31]: '))

# Leap year calculation
leap = False  # Preset leap year value, all this does is remove IDE errors that say 'leap is not defined'
if year % 4 == 0:  # Divisible by 4
    if year % 100 == 0:  # Centurial year, not leap year by default
        if year % 400 == 0:  # If the centurial year is divisible by 400, it's a leap year
            leap = True
        elif year % 400 != 0:
            leap = False
    elif year % 100 != 0:
        leap = True
elif year % 4 != 0:
    leap = False

# Set month length based on input
month_length = 31  # Preset month length, all this does is remove IDE errors that say 'month_length is not defined'
if month < 1 or month > 12:
    print('Please pick a number between 1 and 12 for the different months!')  # Exit with error
elif month == 1:  # January
    month_length = 31
elif month == 2:  # February
    if not leap:  # If it's a common year, February has 28 days
        month_length = 28
    elif leap:  # If it's a leap year, February has 29 days
        month_length = 29
elif month == 3:  # March
    month_length = 31
elif month == 4:  # April
    month_length = 30
elif month == 5:  # May
    month_length = 31
elif month == 6:  # June
    month_length = 30
elif month == 7:  # July
    month_length = 31
elif month == 8:  # August
    month_length = 31
elif month == 9:  # September
    month_length = 30
elif month == 10:  # October
    month_length = 31
elif month == 11:  # November
    month_length = 30
elif month == 12:  # December
    month_length = 31

# Date calculation
if day < 1 or day > month_length:  # Exit with error
    print('Please pick a number between 1 and ' + str(month_length) + '!')
elif 1 <= day <= month_length:
    if day == month_length:
        if month == 12:  # If it's the last day of the month AND it's December, increase year by 1
            day = 1
            month = 1
            year += 1
        elif month != 12:  # If it's the last day of the month, increase month by 1
            day = 1
            month += 1
    elif day != month_length:  # If it's a regular day, increase day by 1
        day += 1
    print('The next date is:')
    print(str(month), str(day), str(year), sep='/')
