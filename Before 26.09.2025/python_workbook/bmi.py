weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in cm): "))

bmi = weight/(height*height/10000)

print("Your BMI is %0.2f" %(bmi))
