fav_fruits = ['banana', 'apple', 'orange']

fruit = 'orange'

if fruit.lower() in fav_fruits:
    print(f"You really like {fruit.title()}s.")
else:
    print(f"You don't like {fruit.title()}s.")
