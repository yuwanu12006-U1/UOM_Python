cities = int(input())
distances = list(map(int, input().split()))

distances.insert(0,0)

relative_distance = 0
for i in range(cities):
    relative_distance -= distances[i]

    reference = relative_distance
    row = []
    for distance in distances:
        displacement = relative_distance + distance
        displacement *= -1 if displacement < 0 else 1
        row.append(displacement)
        relative_distance += distance

    relative_distance = reference
        
    print(row)
