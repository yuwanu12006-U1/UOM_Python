cost = float(input("Enter the cost of food: "))
tax = cost*5/100
tip = cost*18/100

grand = cost + tip + tax

print("Your tax would be %0.2f Rs, Tip %0.2f Rs, and Your Grand total would be %0.2fRs" %(tax, tip, grand))
