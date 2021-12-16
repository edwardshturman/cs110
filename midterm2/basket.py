def main():
    basket = {}
    prices = {'Apple': 0.99,
              'Banana': 1.99,
              'Cherries': 2.99,
              'Avocado': 2.49
              }

    add_to_basket(basket, 'Apple', 2)
    add_to_basket(basket, 'Banana', 1)
    add_to_basket(basket, 'Cherries', 3)
    add_to_basket(basket, 'Avocado', 4)
    add_to_basket(basket, 'Apple', 1)
    add_to_basket(basket, 'Banana', 1)

    show_items(basket)
    total = get_total(basket, prices)
    print('The total cost of all items in the basket: $' + str(format(total, '.2f')))


def show_items(basket):
    print('The fruit and number of each type of fruit in the basket are:')
    for key in basket:
        print('Fruit is: ', key)
        print('Number of fruit are: ', basket[key])
        print()


def add_to_basket(basket, fruit, n):
    if fruit in basket:
        basket[fruit] += n
    else:
        basket[fruit] = n


def get_total(basket, prices):
    total = 0
    for fruit in basket:
        total += (prices[fruit] * basket[fruit])
    return total


main()
