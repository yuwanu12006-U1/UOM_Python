def make_tshirt(size, message):
    '''Create a T-shirt using the size and message user provide'''

    print(f"\nYou're {size.upper()} sized, '{message}' printed tshirt is ready to deliver.")

tshirt_size = input("Enter your size (XS,S,M,L,XL,2XL): ")
printing_message = input("Enter a message you want to print in your T-Shirt: ")

make_tshirt(tshirt_size, printing_message)
make_tshirt(message = printing_message, size = tshirt_size)
