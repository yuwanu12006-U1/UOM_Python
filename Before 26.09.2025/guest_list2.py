guest = ['ramyaa', 'jay', 'yuwan', 'sharu', 'kalai']
print(guest)
print(f"\nBut,")

cannot_make1 = guest.pop(1)
cannot_make2 = guest.pop(-1)

print(f"\tGuests who could make to the Dinner party are {guest}.")
print(f"\t{cannot_make1.title()} and {cannot_make2.title()} cannot make to the dinner tonight.")
print(f"\nSo,")
guest.insert(1, 'jeya')
guest.insert(4, 'mami')
print(f"Our new guests are {guest}")

message = f"\n\tHi {guest[0].title()}, I would like to invite you to a Dinner party."
print(message)
message = f"\n\tHi {guest[1].title()}, I would like to invite you to a Dinner party."
print(message)
message = f"\n\tHi {guest[2].title()}, I would like to invite you to a Dinner party."
print(message)
message = f"\n\tHi {guest[3].title()}, I would like to invite you to a Dinner party."
print(message)
message = f"\n\tHi {guest[4].title()}, I would like to invite you to a Dinner party."
print(message)