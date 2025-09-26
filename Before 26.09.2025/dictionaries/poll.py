favorite_languages = {
    'yuwan': 'python',
    'sarah': 'C',
    'edward' : 'ruby',
    'phil': 'python',
    }

people = ['yuwan', 'ramyaa', 'rukshi', 'sarah', 'edward', 'rashmika', 'dewmina', 'phil',]

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you {person.title()} for responding to the poll, your favorite language is {favorite_languages[person].title()}.")
    else:
        print(f"\t--> Hi {person.title()}, please respond to the poll.")
