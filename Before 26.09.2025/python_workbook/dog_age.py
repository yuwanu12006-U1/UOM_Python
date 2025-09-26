age =int(input())

if 0 < age < 2:
    human_years = age * 10.5
    print(human_years)
    
elif age > 2:
    human_years = (age - 2) * 4 + (2*10.5)
    print(human_years)
    
else:
    print("Your dog not existed yet")
