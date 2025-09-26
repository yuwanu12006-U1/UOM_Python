def make_tshirt(size, message='I love Python'):
    '''Create a T-shirt using the size and message user provide'''

    print(f"\nYour {size.upper()} sized, '{message}' printed tshirt is ready to deliver.")

make_tshirt('M')
make_tshirt('XL')
make_tshirt('L','Hello world!')
make_tshirt(message = 'Hello world!', size = 'M')
