req_toppings = []

if req_toppings:
    for req_topping in req_toppings:
        print(f"Adding {req_topping.title()}.")

    print("\nFinished making your pizza.")

else:
    print("Are you sure you want a plain pizza?")
