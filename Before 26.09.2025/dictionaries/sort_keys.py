favorite_languages = {
    'yuwan': 'python',
    'sarah': 'C',
    'edward' : 'ruby',
    'phil': 'python',
    }
#We can use sorted function to sort in alphabetical order.

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, Thank you for taking the poll.")
