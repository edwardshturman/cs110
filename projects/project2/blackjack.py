import random

MAX = 21


def main():
    hand1 = 0
    hand2 = 0
    deck = create_deck()

    end_game = 0
    while end_game == 0:

        # Game not over yet, continue adding cards
        if hand1 < MAX and hand2 < MAX:
            hand1_card = random.choice(list(deck.keys()))
            hand2_card = random.choice(list(deck.keys()))
            print('Player 1 was dealt a(n) ' + hand1_card)
            print('Player 2 was dealt a(n) ' + hand2_card)
            hand1_card_value = deck[hand1_card]
            hand2_card_value = deck[hand2_card]
            hand1 = update_hand_value(hand1, hand1_card_value, hand1_card)
            hand2 = update_hand_value(hand2, hand2_card_value, hand2_card)
            print('Player 1\'s new hand value is ' + str(hand1))
            print('Player 2\'s new hand value is ' + str(hand2))
            end_game = 0

        # Tie
        elif hand1 >= MAX and hand2 >= MAX:
            print('There is no winner.')
            end_game = 1

        # Player 1 wins
        elif hand1 >= MAX > hand2:
            print('Player 1 wins!')
            end_game = 1

        # Player 2 wins
        elif hand1 < MAX <= hand2:
            print('Player 2 wins!')
            end_game = 1


def create_deck():
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    special_values = {'Ace': 1, 'King': 10, 'Queen': 10, 'Jack': 10}

    numbers = ['Ace', 'King', 'Queen', 'Jack']
    for i in range(2, 11):
        numbers.append(i)

    deck = {}
    for suit in suits:

        for num in numbers:
            if type(num) == int:
                deck.update({str(num) + ' of ' + suit: num})

        for special_value in special_values:
            deck.update({special_value + ' of ' + suit: special_values[special_value]})

    return deck


def update_hand_value(hand, value, card):
    if 'Ace' in card:
        value = 11
        hand += value
        if hand > MAX:
            hand -= 10
            return hand
        else:
            return hand
    else:
        hand += value
        return hand


main()
