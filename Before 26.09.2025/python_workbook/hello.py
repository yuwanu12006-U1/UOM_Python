active = True
while active:
    name = input("Enter your naame or enter 'q' to quit: ")
    if name != 'q':
        print(f"Hello {name.title()}!")
    else:
        active = False
