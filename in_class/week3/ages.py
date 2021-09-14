# Write a Python program ages.py where the user enters their age and their friend's age. If the user's age is bigger
# or equal to their friend's age, print 'You are older or the same age as your friend.' If the friend is older,
# print 'Your friend is older than you.'


user_age = int(input('What is your age? '))
friend_age = int(input('What is your friend\'s age? '))
if user_age >= friend_age:
    print('You are older or the same age as your friend.')
elif friend_age > user_age:
    print('Your friend is older than you.')
else:
    print('Error in calculation.')
