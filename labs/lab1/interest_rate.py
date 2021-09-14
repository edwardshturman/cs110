# Set starting interest rate
interest_rate = 3.5  # Type float

# User questions
age = int(input('What is your age? '))
marital_status = input('Are you married? [y]/[n] ')
credit_score = int(input('What is your credit score? '))

# Age check
if age < 25:
    interest_rate += 1.5
elif age >= 50:
    interest_rate -= 0.5

# Marital status check
if marital_status == 'y':
    interest_rate -= 0.75

# Credit score check
if credit_score < 550:
    interest_rate += 2.5
elif 550 <= credit_score < 650:
    interest_rate += 1.5
elif credit_score >= 650:
    interest_rate -= 0.5

# Display final interest rate
print('Your interest rate is: ' + str(interest_rate) + '%.')
