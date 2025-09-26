while True:
    user = input("Enter your age or Enter 'quit' to exit the program: ")
    if user == 'quit':
        break
    try:
        age = int(user)
        if age <= 0:
            print("Input a valid age")
            continue
        elif age < 3:
            print("Your ticket is free!")
            continue
        elif age < 12:
            print("Your ticket charge is $10")
            continue
        else:
            print("Your ticket charge is $15")
            continue
    except ValueError:
        print("Enter only how many years you are old.")
