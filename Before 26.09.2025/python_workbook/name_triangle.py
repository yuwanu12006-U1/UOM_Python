length1 = float(input())
length2 = float(input())
length3 = float(input())

if length1 == length2 and length1 == length3:
    print('equilatarel')

elif length1 == length2 or length1 == length3 or length2 == length3:
    print('isosceles')

elif length1 != length2 and length1 != length3 and length2 != length3:
    print('scalene')
