rivers = {
    'nile': 'egeypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'danube': 'germany',
    'ganga': 'india',
    }

for river, country in rivers.items():
    print(f"\nThe {river.title()} river runs through {country.title()}.")

print("\nThese are the mentioned rivers:")

for riv in rivers.keys():
    print(riv.title())

print("\nThese are the mentioned Countries:")

for country in rivers.values():
    print(country.title())
