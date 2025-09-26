def greet_users(names):
    '''print a simple greeting message to each user in the list.'''
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['yuwan','rukshi','aadhya']
greet_users(usernames)
