def describe_city(city, country = 'sri lanka'):
    '''Tells provided city is in provided country.'''
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('Kotagala')
describe_city('Gampaha')
describe_city(country='India', city='Chennai')
