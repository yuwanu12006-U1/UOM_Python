active = True
while active:
    toppings = input("Enter toppings you like: ")
    if toppings != 'quit' : print(f"I'll add {toppings.title()} to your pizza.")
    else: active = False
