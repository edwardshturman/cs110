# Inputs:
# ROCK = 1
# PAPER = 2
# SCISSORS = 3

# Results:
# TIE
# COMPUTER_WINS
# PLAYER_WINS
# INVALID


def main():
    tie = 1
    while tie == 1:
        print('Welcome to Rock, Paper, Scissors!')

        # Get user input
        player = int(input('Enter 1 for rock, 2 for paper, 3 for scissors: '))

        # Generate random number
        import random
        computer = random.randint(1, 3)

        # Print player hand
        choice = player
        result = choice_string(choice)
        print('Player chose: ' + str(result))

        # Print computer hand
        choice = computer
        result = choice_string(choice)
        print('Computer chose: ' + str(result))

        # Run round and print result
        result = rock_paper_scissors(computer, player)
        if result == 'TIE':
            tie = 1  # Run the game again
            print('You made the same choice as the computer. Starting over....')
        elif result == 'COMPUTER_WINS':
            tie = 0  # Won't loop the game again
            print('The computer wins the game. Better luck next time!')
        elif result == 'PLAYER_WINS':
            tie = 0  # Won't loop the game again
            print('You win the game, congratulations!')
        elif result == 'INVALID':
            tie = 0  # Won't loop the game again
            print('You made an invalid choice. No winner.')


def rock_paper_scissors(computer, player):
    if computer == 1:  # Computer chooses rock
        if player == 1:  # Player chooses rock
            result = 'TIE'
            return result
        elif player == 2:  # Player chooses paper
            result = 'PLAYER_WINS'
            return result
        elif player == 3:  # Player chooses scissors
            result = 'COMPUTER_WINS'
            return result
        else:
            result = 'INVALID'
            return result
    elif computer == 2:  # Computer chooses paper
        if player == 1:  # Player chooses rock
            result = 'COMPUTER_WINS'
            return result
        elif player == 2:  # Player chooses paper
            result = 'TIE'
            return result
        elif player == 3:  # Player chooses scissors
            result = 'PLAYER_WINS'
            return result
        else:
            result = 'INVALID'
            return result
    elif computer == 3:  # Computer chooses scissors
        if player == 1:  # Player chooses rock
            result = 'PLAYER_WINS'
            return result
        elif player == 2:  # Player chooses paper
            result = 'COMPUTER_WINS'
            return result
        elif player == 3:  # Player chooses scissors
            result = 'TIE'
            return result
        else:
            result = 'INVALID'
            return result
    else:
        result = 'INVALID'
        return result


def choice_string(choice):
    if choice == 1:
        result = 'Rock'
        return result
    elif choice == 2:
        result = 'Paper'
        return result
    elif choice == 3:
        result = 'Scissors'
        return result
    else:
        result = 'Something went wrong!'
        return result


main()
