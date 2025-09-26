guest = ['ramyaa', 'jay', 'rukshi', 'sharu', 'kalai']
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

print("\nI found a bigger dining table. So we could call another 3 guests to the dinner tonight.")
guest.append('siva')
guest.append('ruby')
guest.append('arumugam')
print(f"\nfinally all of our guests are {guest}")

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
message = f"\n\tHi {guest[5].title()}, I would like to invite you to a Dinner party."
print(message)
message = f"\n\tHi {guest[6].title()}, I would like to invite you to a Dinner party."
print(message)
message = f"\n\tHi {guest[7].title()}, I would like to invite you to a Dinner party."
print(message)

print(guest)
print("\nI just found out that my new dinner table won't arrive in time for the dinner, and unfortunately i have space for only three guests.")
no = guest.pop(1)
print(f"\nI'm Sorry {no.title()}, I can't invite you to Dinner party tonight.")
no = guest.pop(2)
print(f"\nI'm Sorry {no.title()}, I can't invite you to Dinner party tonight.")
no = guest.pop(3)
print(f"\nI'm Sorry {no.title()}, I can't invite you to Dinner party tonight.")
no = guest.pop(3)
print(f"\nI'm Sorry {no.title()}, I can't invite you to Dinner party tonight.")
no = guest.pop(3)
print(f"\nI'm Sorry {no.title()}, I can't invite you to Dinner party tonight.")
print(f"\nUnfortunately i could invite only {guest} to the dinner party tonight.")

print("\nSadly i burnt the food. So i can't organize a Dinner party. So no party tonight :(")
del guest[0]
del guest[1]
print("Finally... Tonight I could only Invite,")
print(f"\t{guest[0].title()}")