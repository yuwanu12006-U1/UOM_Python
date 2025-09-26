glossary = {
    'python': 'High level General-purpose programming language.',
    'operator': 'A symbol or function denoting an operation (eg: +,*)',
    'list': 'A built in data type used to store multiple items in a single variable.',
    'tuple': 'Tuple is an unchangable collection of various data type elements',
    'dictionary': 'A data structure that stores items in key-value pairs.',
    'set': 'A data type in python used to store several items in a single variable.',
    'integer': 'A whole number, positive or negative, without decimals.',
    }

print("This is my programming Glossary")

for word, meaning in glossary.items():
    print(f"\n{word.title()}")
    print(f"\t{meaning.title()}")
