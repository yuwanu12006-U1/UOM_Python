weight = float(input("Enter weight of your water you need to heatup (in grams): "))
current_temperature = float(input("Enter the current temperature of water (in celcius or Kelvin): "))
hot_temperature = float(input("Enter the temperature of water you want (in celcius or Kelvin): "))

if hot_temperature < current_temperature:
    print("You cannot cool down with a heater")
    
heat = weight * 4.186 * (hot_temperature - current_temperature)

if heat > 1000:
    print(heat/1000, "Kilojoules")
else:
    print(heat, "Joules")

cost = (heat / 3600000) * 15
print("This costs: %0.2f Rs" %(cost)) 
