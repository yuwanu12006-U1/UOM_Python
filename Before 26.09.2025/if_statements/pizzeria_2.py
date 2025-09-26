req_toppings = ['mushrooms','green peppers', 'extra cheese']

for req_topping in req_toppings:
    if req_topping == 'green peppers':
        print("Sorry, we are out of Green Peppers right now.")
    else:
        print(f"Adding {req_topping.title()}.")

print("Finished making your pizza!")
