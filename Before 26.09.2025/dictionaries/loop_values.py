favorite_languages = {
    'yuwan': 'python',
    'sarah': 'C',
    'edward' : 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(f"\t{language.title()}")

# This approach pulls all the values from the dictionary without checking for repeats.
# Instead we can use set function.

print("\nBy using set function,")
for lang in set(favorite_languages.values()):
    print(f"\t{lang.title()}")
