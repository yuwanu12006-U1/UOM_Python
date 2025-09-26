current_users = ['yuwan','ramyaa','rukshi','kalai','john']

new_users = ['rivija', 'sahas', 'RuKsHi', 'Ramyaa']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Username {new_user.title()} is unavailable.")
    else:
        print(f"Username {new_user.title()} is Available.")
