h = float(input("Enter the height (in meters): "))
v = float(input("Enter the starting velocity (in m/s): "))

v_f = (v**2 +2*9.8*h)**0.5
print("Freefall velocity of object when reaching land: %0.2f m/s" %(v_f))
