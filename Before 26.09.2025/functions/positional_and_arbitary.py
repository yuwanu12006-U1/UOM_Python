#Arbitary parameter must be in last position
def make_pizza(size, *toppings):
    '''summarize the pizza we are about to make.'''
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping.title()}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'cheese', 'sausages')
