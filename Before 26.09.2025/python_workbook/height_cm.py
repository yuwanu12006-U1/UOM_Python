height = input("Enter your height in feet and inches (Eg: 5 11): ").split()

height_cm = int(height[0])*12*2.54 + int(height[1])*2.54
print(height_cm, 'cm')
