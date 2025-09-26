less_deposit = 0.1
more_deposit = 0.25

less = int(input("How many 1L or less bottle do you have? "))
more = int(input("How many more than 1L bottle do you have? "))

refund = less*less_deposit + more*more_deposit
print("You earned $%0.2f by recycling" %(refund))
