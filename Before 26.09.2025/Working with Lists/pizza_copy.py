pizzas = ['cheese pizza', 'pepperoni pizza', 'pan pizza']
for pizza in pizzas:
    print(pizza.upper())
    print(f"\ti like {pizza}.\n".title())
print('I Really Love Pizzas.')

my_pizzas = pizzas
friend_pizzas = my_pizzas[:]

my_pizzas.append('bbq pizza')
my_pizzas.append('black chicken pizza')

friend_pizzas.append('veg pizza')

print("\nMy favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza.title())

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
