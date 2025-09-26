age = 20

if age < 4:
    price = 0

elif age < 18:
    price = 25

elif age > 45:
    price = 30
    
else:
    price = 45

print(f"Your admission cost is ${price}.")

if 18 <= age < 45:
    print(f"If you come with your partner it'll be cost ${price*2-10} for both.")
