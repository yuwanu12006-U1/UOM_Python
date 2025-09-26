def print_models(unprinted_designs, completed_models):
    '''
    simulate printing each design, until non are left.
    move each design to completed_models after printing.
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''Show all the models that were printed.'''
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(f'\t{model.title()}')

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
