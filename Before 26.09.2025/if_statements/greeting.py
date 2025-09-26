users = ['admin','yuwan','ramyaa','rukshi','kalai']

for user in users:
    if user == 'admin':
        print(f"Hello {user.title()}, Greetings! would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, Greetings! Thank you for logging in again.")
