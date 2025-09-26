def get_full_name(first_name, last_name, middle_name=''):
    '''Return Full name, neatly formatted.'''
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"

    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

name = get_full_name('yuwan','kalaiyarasu','sri')
print(name)

name = get_full_name('yuwan', 'sri')
print(name)
