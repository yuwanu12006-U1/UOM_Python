pets = ['dog', 'cat', 'dog', 'goldfish', 'cat',
        'rabbit', 'cat', 'parrot', 'parrot', 'snake', 'frog', 'frog']
[print(pet) for pet in pets]

pet_set = []
for _ in range(len(pets)):
    for pet in pets:
        while pet in pets:
            pets.remove(pet)

        pet_set.append(pet)
        break

print(pet_set)
