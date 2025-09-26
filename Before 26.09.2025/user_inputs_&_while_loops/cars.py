cars = ['bmw','benz','ford','subaru','porsche','mitsubishi']
car=input("What kind of car would you like to rent? ")

if car.lower() in cars:
    print(f"Let me see if I can find you a {car.title()}.")

else:
    print("Requested car is not in our car collection.")
