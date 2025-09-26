rukshi = {
    'first_name': 'Rukshika',
    'last_name': 'Yuwan Sri',
    'age': 23,
    'city': 'Lindula',
    }

yuwan = {
    'first_name': 'Yuwan',
    'last_name': 'Sri',
    'age': 22,
    'city': 'Kotagala',
    }

ramyaa = {
    'first_name': 'Ramyaa',
    'last_name': 'Shri',
    'age': 15,
    'city': 'Kotagala',
    }

people = [rukshi,yuwan,ramyaa]

for person in people:
    print(f"\nFullname: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")
