unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop(0)
    print(f"Printing model: {current_design.title()}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for model in completed_models:
    print(f"\t{model.title()}")
