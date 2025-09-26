import math

point1 = list(map(float, input("Input a longitude and latitude of a point spereated by ',': ").split(',')))
point2 = list(map(float, input("Input another longitude and latitude of a point spereated by ',': ").split(',')))

t1 = math.radians(point1[0])
g1 = math.radians(point1[1])
t2 = math.radians(point2[0])
g2 = math.radians(point2[1])

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print("%0.2f kms" %(distance))
