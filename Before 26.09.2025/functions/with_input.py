def describe_pet(animal_type, pet_name):
    '''Display information about a Pet.'''
    print(f"\nI have a {animal_type.title()}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

animal = input()
name =input()

if animal != '' and name != '':
    try:
        describe_pet(animal, name)

    except TypeError:
        print("Provide the details needed, no more or no less")
else:
    print("Provide the details needed, no more or no less")
