one_bottle_count = 0
big_bottle_count = 0

prompt = "Enter the volume of bottles you recycled (in liters)\nEnter '0' when you finished: "
while True:
    litre = float(input(prompt))
    if 0 < litre < 1:
        print("\tYou don't get any refund for this recycle\n")
    elif litre == 1:
        one_bottle_count += 1
        print("\tYou get a $0.10 refund for this recycle\n")
    elif litre > 1:
        big_bottle_count += 1
        print("\tYou get a $0.25 refund for this recycle\n")
    elif litre == 0:
        break
    else:
        print("\tPlease enter a valid volume\n")

print("Your final earning")
print(f"$%0.2f, Thank you! come again." %(one_bottle_count*0.1 + big_bottle_count*0.25)) 
