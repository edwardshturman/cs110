import random


def play_guessing_game(number):
    guess = int(input('Enter a number between 1 and 20, or 0 to quit: '))
    if guess == 0:
        return guess
    elif guess < number:
        print('Too low, try again.')
        return guess
    elif guess > number:
        print('Too high, try again.')
        return guess
    elif guess == number:
        print('Congratulations, you guessed the right number!')
        return guess


def main():
    number = random.randint(1, 20)
    guess = play_guessing_game(number)
    while guess != 0:
        guess = play_guessing_game(number)
        if guess == number:
            print('Generating a new number....')
            number = random.randint(1, 20)
            guess = play_guessing_game(number)
    print('Thanks for playing!')


main()
