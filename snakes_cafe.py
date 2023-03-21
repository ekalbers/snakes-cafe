from textwrap import dedent

intro = dedent(
    '''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **                                  **
    ** To quit at any time, type "quit" **
    **************************************
    '''
)

menu = dedent(
    '''
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    '''
)

order = dedent(
    '''
    ***********************************
    ** What would you like to order? **
    ***********************************
    '''
)

orderElse = dedent(
    '''
    ****************************************
    ** What else would you like to order? **
    ****************************************
    '''
)

closing = dedent(
    '''
    ***********************************
    **    Thanks for swinging by!    **
    ***********************************
    '''
)

orderTracker = {
    'wings': 0,
    'cookies': 0,
    'spring rolls': 0,
    'salmon': 0,
    'steak': 0,
    'meat tornado': 0,
    'a literal garden': 0,
    'ice cream': 0,
    'cake': 0,
    'pie': 0,
    'coffee': 0,
    'tea': 0,
    'unicorn tears': 0
}


def main():
    print(intro)
    print(menu)
    print(order)

    while True:
        item = input('> ')
        item = item.lower()
        if item == 'quit':
            break

        if item not in orderTracker.keys():
            print('** Unfortunately that is not on the menu **')
        else:
            orderTracker[item] += 1
            if orderTracker[item] == 0:
                print(f'** {orderTracker[item]} order of {item} added to your order')
            else:
                print(f'** {orderTracker[item]} orders of {item} have been added to your order')
        print(orderElse)

    print(closing)


if __name__ == '__main__':
    main()
