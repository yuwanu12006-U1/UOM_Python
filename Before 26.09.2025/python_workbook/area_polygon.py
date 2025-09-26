import math

sides = int(input("How many sides your polygon have?"))
length = float(input("Length of a side (in cm): "))

pi = math.pi

area = (sides * length ** 2)/(4 * math.tan(pi/4))
print("Area = %0.2f sqr cms"%(area))
