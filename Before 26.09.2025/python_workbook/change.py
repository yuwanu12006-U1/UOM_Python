amount = int(input())

cashes = [5000,1000,500,100,50,20,10,5,2,1]
changes = []

for cash in cashes:
    cash_count=0
    while amount//cash != 0:
        cash_count += 1
        amount -= cash
    changes.append([cash, cash_count])

for change in changes:
    if change[1] != 0:
        print(change[0], ':', change[1])
