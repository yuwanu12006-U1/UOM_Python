def format_name(first_name, last_name):
    '''Return full name neatly formatted.'''
    full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = format_name('yuwan', 'sri')
print(musician)
