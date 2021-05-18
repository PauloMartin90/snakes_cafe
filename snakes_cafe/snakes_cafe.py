
FULL_WIDTH = 38


store_info = [ 
    "Welcome to the Snakes Cafe!",
    "Please see our menu below.",
    " ",
    'To quit at any time, type "quit"'
    ]

menu_items = {
    "Appetizers": ['Wings', 'Cookies', 'Spring Rolls'], 
    "Entrees": ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
    "Desserts": ['Ice Cream', 'Cake', 'Pie'],
    "Drinks": ['Coffee', 'Tea', 'Unicorn Tears']
    }

# Greeting
def greeting(texts, width):
    print("*" * width )
    for text in texts:
        print("**" + text.center(width-4) + "**")
    print("*" * width )


# Display Menu
def display_menu(menus):
    for category in menus:
        print(category)
        print("-"*len(category))
        meals = menus[category]

        for meal in meals:
            print(meal)
        print(" ")

# Display Order
def display_order(width):
    order_greeting = "What would you like to order? "
    print("*" * width)
    print("**" + order_greeting.center(width-4) + "**")
    print("*" * width)

# Order Confirmed
def order_confirmed(response, order):
    print(f'** {order[response]} order of {response} have been added to your meal **\n')


# Heading Information
greeting(store_info, FULL_WIDTH)
display_menu(menu_items)
display_order(FULL_WIDTH)



running = True
order = {}
while running:
    response = input('> ')
    if response == 'quit':
        full_order = ''
        if order:
            for item in order:
                full_order+=f'{order[item]} {item}, '
        print(f'Your order is: {full_order}')
        running = False
    elif response in order:
        order[response]+=1
        order_confirmed(response, order)
    else:
        order[response] = 1
        order_confirmed(response, order)




