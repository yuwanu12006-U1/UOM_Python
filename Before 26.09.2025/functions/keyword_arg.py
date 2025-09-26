def describe_pet(animal_type, pet_name):
    '''Display information about a Pet.'''
    print(f"\nI have a {animal_type.title()}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

#Order doesn't matter but We need to type the parameters exactly same.
describe_pet(animal_type='German Shepord', pet_name = 'Daisy')
describe_pet(pet_name = 'Roy', animal_type = 'Golden Shepord')
