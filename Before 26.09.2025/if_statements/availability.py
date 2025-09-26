available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'frech fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping.title()}.")
    else:
        print(f"Sorry, we don't have {requested_topping.title()}.")

print("\nFinished making your pizza!")
