def describe_pet(animal_type, pet_name):
    '''Display information about a Pet.'''
    print(f"\nI have a {animal_type.title()}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('German shepord', 'Daisy')
describe_pet('Cross bread', 'Stuart')
describe_pet('Golden Shepord', 'Roy')
