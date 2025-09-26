h = int(input())
# Assuming 'spaces' is initialized to a single space character for multiplication
spaces = ' ' 

for a in range(h + 1):
    stars = '*' * a
    spaces = ' ' * (h - a) # This is effectively what spaces *= (h-a) does if spaces was ' '

    print(spaces, end='')
    print(stars, end='')
    if (a > 0):
        print(' | ', end='')
    else:
        print(' * ', end='')
    print(stars, end='')
    print(spaces) # This prints spaces on a new line, which is unusual for a tree
