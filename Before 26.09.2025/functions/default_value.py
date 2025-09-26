#Parameters with default values must be positioned in last.
def describe_pet(pet_name, animal_type='dog'):
    '''Display information about a Pet.'''
    print(f"\nI have a {animal_type.title()}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='Stuart')
#We can only provide the name, no need to provide type.
describe_pet('Roy')
describe_pet(pet_name='Harry', animal_type='Hamster')
