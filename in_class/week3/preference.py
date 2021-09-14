# Write a Python program preference.py to:
# Ask the user 'How much do you like pizza on a scale of 1 (hate) to 5 (love)?'
# Ask the user 'How much do you like tacos on a scale of 1 (hate) to 5 (love)?'
# If users like pizza more than tacos, print 'You like pizzas more than tacos.' (You do not need an else condition.)


pizza_preference = int(input('How much do you like pizza, on a scale of 1 (hate) to 5 (love)? '))
taco_preference = int(input('How much do you like tacos, on a scale of 1 (hate) to 5 (love)? '))
if pizza_preference > taco_preference:
    print('You like pizza more than tacos.')
