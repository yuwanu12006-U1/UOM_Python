banned_users = ['andrew', 'carolina', 'david']

user_1 = 'marie'
if user_1 not in banned_users:
    print(f"{user_1.title()}, you can post a response if you wish.")

user_2 = 'andrew'
if user_2 not in banned_users:
    print(f"{user_2.title()}, you can post a response if you wish.")
else:
    print(f"{user_2.title()}, you cannot post a response, your account is banned.")

user_3 = 'ramyaa'
if user_3 not in banned_users:
    print(f"{user_3.title()}, you can post a response if you wish.")
else:
    print(f"{user_3.title()}, you cannot post a response, your account is banned.")
